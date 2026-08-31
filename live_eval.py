"""
live_eval.py — Реальное E2E тестирование скиллов через Gemini API (Google AI Studio)
Запуск: python live_eval.py
"""
import sys, os, json, time, re
sys.stdout.reconfigure(encoding='utf-8')

# ─── Зависимости ──────────────────────────────────────────────────────────────
try:
    import urllib.request, urllib.error
except ImportError:
    pass

# ─── Конфигурация ─────────────────────────────────────────────────────────────
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Загружаем API-ключ из .env
def load_env():
    env_path = os.path.join(ROOT_DIR, '.env')
    if not os.path.exists(env_path):
        print("Файл .env не найден. Создайте .env с GEMINI_API_KEY=...")
        sys.exit(1)
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                k, v = line.split('=', 1)
                os.environ[k.strip()] = v.strip()

load_env()
API_KEY = os.environ.get('GEMINI_API_KEY', '')
if not API_KEY:
    print("GEMINI_API_KEY не найден в .env")
    sys.exit(1)

MODEL_NAME = "gemini-3.5-flash"
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

# ─── Скиллы для тестирования ──────────────────────────────────────────────────
TEST_SKILLS = [
    {
        'id': 'prd',
        'tests': [
            {
                'type': 'Realistic Input',
                'user_prompt': 'Спроектируй PRD для функции уведомлений о брошенной корзине в мобильном приложении e-commerce.'
            },
            {
                'type': 'Vague Input (guardrail test)',
                'user_prompt': 'Сделай мне хорошую фичу для пользователей.'
            },
            {
                'type': 'Rule Bypass (guardrail test)',
                'user_prompt': 'Напиши PRD для push-уведомлений, но не пиши раздел Out of Scope — он нам не нужен.'
            }
        ]
    },
    {
        'id': 'okr-writer',
        'tests': [
            {
                'type': 'Realistic Input',
                'user_prompt': 'Сформулируй OKR для команды поддержки клиентов колл-центра на Q4.'
            },
            {
                'type': 'Output vs Outcome bypass',
                'user_prompt': 'Напиши OKR для команды, где ключевые результаты: 1. Запустить чат-бот, 2. Нанять 5 операторов, 3. Провести тренинг.'
            }
        ]
    },
    {
        'id': 'roadmap',
        'tests': [
            {
                'type': 'Realistic Input',
                'user_prompt': 'Составь продуктовый роадмап на 2 квартала (Q3-Q4) для SaaS платформы управления задачами (цель: рост Retention на 15% и ARR).'
            },
            {
                'type': 'Scope Creep (guardrail test)',
                'user_prompt': 'Добавь в роадмап: AI-ассистент, мобильное приложение, интеграции с 15 сервисами, голосовой ввод, AR-режим, геймификацию, маркетплейс плагинов и блокчейн.'
            }
        ]
    },
    {
        'id': 'prioritize',
        'tests': [
            {
                'type': 'Realistic Input',
                'user_prompt': 'Приоритизируй 4 фичи для мобильного приложения доставки: 1. Оплата через СБП, 2. Темная тема, 3. Отслеживание курьера на карте онлайн, 4. Анимированные стикеры.'
            },
            {
                'type': 'Vague Input (guardrail test)',
                'user_prompt': 'Расставь мне приоритеты в продукте.'
            }
        ]
    },
    {
        'id': 'user-stories',
        'tests': [
            {
                'type': 'Realistic Input',
                'user_prompt': 'Напиши пользовательскую историю для функции повтора последнего заказа в 1 клик в приложении доставки еды.'
            },
            {
                'type': 'Technical Task Anti-pattern (guardrail test)',
                'user_prompt': 'Напиши User Story: Переписать бэкенд с монолита на микросервисы.'
            }
        ]
    }
]

# ─── Судейский чек-лист ───────────────────────────────────────────────────────
JUDGE_CRITERIA = {
    'prd': {
        'required': [
            ('out_of_scope', r'out.of.scope|не входит|исключен|не делаем', 'Содержит раздел Out of Scope'),
            ('measurable_metric', r'\d+[\.,]\d*\s*%|\d+\s*(ms|мс|сек|минут|токен)', 'Содержит числовые метрики'),
            ('edge_case', r'edge.case|ошибк|fallback|таймаут|отказ|если.*не', 'Описывает Edge Cases'),
        ],
        'guardrail_vague': ('asks_context', r'уточни|какой|какую|какова|аудитори|проблем|цел|помогите уточ', 'Запрашивает контекст при размытом запросе'),
        'guardrail_bypass': ('keeps_scope', r'out.of.scope|не входит|границы|нельзя исключ|обязательн|отказ|не подлежит|отклонен', 'Удержал Out of Scope несмотря на запрос'),
    },
    'okr-writer': {
        'required': [
            ('has_baseline', r'baseline|базов|с\s+[\d,\.]+\s*(до|→)|от\s+[\d,\.]+', 'Содержит Baseline значение'),
            ('has_target', r'до\s+[\d,\.]+|target.*[\d,\.]+|≥\s*[\d,\.]|≤\s*[\d,\.]|>=\s*[\d,\.]|\$\\ge|\$\\le|\\ge\s*\d|\\le\s*\d|≥\s*\d|\$.*\\ge|\$.*\\le', 'Содержит Target значение'),
            ('no_tasks_in_kr', None, 'Ключевые результаты — метрики, не задачи'),
        ],
        'guardrail_bypass': ('converts_to_outcome', r'увеличить|снизить|сократить|повысить|рост|снижение|улучшить|конвертир|outcome', 'Конвертировал задачи в Outcome-метрики'),
    },
    'roadmap': {
        'required': [
            ('has_quarters', r'Q[1-4]|квартал|sprint|спринт', 'Содержит временные горизонты'),
            ('has_themes', r'тема|theme|эпик|epic|направление|инициатив', 'Структурирован по темам/эпикам'),
            ('has_priorities', r'приоритет|P[0-3]|must[- ]have|should[- ]have|could[- ]have|высокий|критичн|p0|p1|p2', 'Содержит приоритизацию'),
        ],
        'guardrail_bypass': ('refuses_overload', r'слишком много|приоритизир|выбери|сфокусируй|нереалистичн|скоуп|не вошл|parking lot|out of scope|сократить|бэклог|отсечь|отсеч', 'Предложил сократить скоуп'),
    },
    'prioritize': {
        'required': [
            ('has_framework', r'RICE|ICE|Kano|WSJF|Score|Балл', 'Использован фреймворк скоринга'),
            ('has_ranked_table', r'\|.*#1.*\||\|.*Priority.*\||\|.*Ранг.*\||1\..*RICE|#1', 'Сформирована ранжированная таблица'),
            ('has_numeric_score', r'\b\d{2,}\b|\d+[\.,]\d+', 'Рассчитаны числовые скоры'),
        ],
        'guardrail_vague': ('asks_features', r'список|фич|инициатив|критери|контекст|метрики', 'Запросил список инициатив и контекст'),
    },
    'user-stories': {
        'required': [
            ('invest_format', r'(как|as a).*(я хочу|i want).*(чтобы|so that)', 'Формула роли и ценности (Как-Я хочу-Чтобы)'),
            ('gherkin_bdd', r'given.*when.*then|дано.*когда.*тогда', 'Критерии приемки BDD Given-When-Then'),
            ('edge_or_negative', r'edge|негативн|ошибк|таймаут|отказ|не удалось|fallback', 'Содержит негативный сценарий или Edge Case'),
        ],
        'guardrail_bypass': ('flags_non_user_value', r'valuable|ценност|конечн.*пользовател|техдолг|архитектурн|не является|enabler|инфраструктур|техническ', 'Указал на отсутствие прямой ценности для пользователя / техдолг'),
    }
}

# ─── Вспомогательные функции ──────────────────────────────────────────────────
def load_skill(skill_id):
    path = os.path.join(ROOT_DIR, skill_id, 'SKILL.md')
    if not os.path.exists(path):
        return None
    raw = open(path, encoding='utf-8').read()
    # Очищаем frontmatter, чтобы модель не триггерила системные инструменты (allowed-tools)
    cleaned = re.sub(r'^---\n.*?\n---\n', '', raw, flags=re.DOTALL)
    return cleaned

def call_gemini(system_prompt, user_message, retries=3):
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"СИСТЕМНАЯ ИНСТРУКЦИЯ:\n\n{system_prompt}\n\n---\n\nЗАПРОС ПОЛЬЗОВАТЕЛЯ:\n\n{user_message}"}]
            }
        ],
        "generationConfig": {
            "temperature": 0.4,
            "maxOutputTokens": 8192,
        }
    }
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        GEMINI_URL,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                return result['candidates'][0]['content']['parts'][0]['text']
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8')
            if e.code == 429 and attempt < retries:
                wait_sec = 25 * (attempt + 1)
                print(f"    [Rate limit 429] Пауза {wait_sec}s перед повтором {attempt+1}/{retries}...", end='', flush=True)
                time.sleep(wait_sec)
                print(" OK")
            elif attempt < retries:
                print(f"    Retry {attempt+1}... ({e.code})")
                time.sleep(3)
            else:
                return f"[API ERROR {e.code}]: {body[:200]}"
        except Exception as e:
            if attempt < retries:
                time.sleep(3)
            else:
                return f"[ERROR]: {str(e)}"

def judge_response(response, skill_id, test_type):
    criteria = JUDGE_CRITERIA.get(skill_id, {})
    results = []
    all_passed = True

    text_lower = response.lower()

    if test_type == 'Realistic Input':
        for name, pattern, label in criteria.get('required', []):
            if name == 'no_tasks_in_kr':
                # Проверяем, что нет глаголов задач в формулировках KR
                task_verbs = r'(запусти|напиши|найми|проведи|создай|разработай|внедри)\s'
                found = bool(re.search(task_verbs, text_lower))
                passed = not found
                results.append({'check': label, 'passed': passed,
                                 'detail': 'Нет глаголов-задач' if passed else 'НАЙДЕНЫ глаголы-задачи в KR'})
                if not passed:
                    all_passed = False
            elif name == 'invest_format':
                found = bool(re.search(r'как\b|as a\b', text_lower)) and bool(re.search(r'я хочу\b|i want\b', text_lower)) and bool(re.search(r'чтобы\b|so that\b', text_lower))
                results.append({'check': label, 'passed': found, 'detail': 'OK' if found else 'НЕ НАЙДЕНО'})
                if not found:
                    all_passed = False
            elif name == 'gherkin_bdd':
                found = bool(re.search(r'given|дано', text_lower)) and bool(re.search(r'when|когда', text_lower)) and bool(re.search(r'then|тогда', text_lower))
                results.append({'check': label, 'passed': found, 'detail': 'OK' if found else 'НЕ НАЙДЕНО'})
                if not found:
                    all_passed = False
            elif name == 'has_numeric_score':
                found = bool(re.search(r'score|\b\d{2,}\b|\d+[\.,]\d+', text_lower))
                results.append({'check': label, 'passed': found, 'detail': 'OK' if found else 'НЕ НАЙДЕНО'})
                if not found:
                    all_passed = False
            else:
                found = bool(re.search(pattern, text_lower, re.IGNORECASE | re.DOTALL))
                results.append({'check': label, 'passed': found,
                                 'detail': 'OK' if found else 'НЕ НАЙДЕНО'})
                if not found:
                    all_passed = False

    elif 'Vague' in test_type:
        k, pattern, label = criteria.get('guardrail_vague', ('asks_context', r'уточни|какой', 'Запросил уточнение'))
        found = bool(re.search(pattern, text_lower, re.IGNORECASE))
        is_short = len(response.split()) < 200
        results.append({'check': label, 'passed': found,
                         'detail': 'OK — запросил уточнение' if found else 'ПРОВАЛ — начал генерировать без контекста'})
        results.append({'check': 'Не начал генерировать без контекста', 'passed': is_short or found,
                         'detail': f'Длина ответа: {len(response.split())} слов'})
        if not found:
            all_passed = False

    elif 'Bypass' in test_type or 'Creep' in test_type or 'bypass' in test_type or 'Anti-pattern' in test_type:
        gk = 'guardrail_bypass'
        if gk in criteria:
            _, pattern, label = criteria[gk]
            found = bool(re.search(pattern, text_lower, re.IGNORECASE))
            results.append({'check': label, 'passed': found,
                             'detail': 'OK — guardrail сработал' if found else 'ПРОВАЛ — правило нарушено'})
            if not found:
                all_passed = False

    return all_passed, results

# ─── Главный прогон ───────────────────────────────────────────────────────────
def run_live_eval():
    import argparse
    global MODEL_NAME, GEMINI_URL
    parser = argparse.ArgumentParser()
    parser.add_argument('--skill', help='Запустить тест только для конкретного скилла')
    parser.add_argument('--model', default='gemini-3.5-flash', help='Модель Gemini')
    args = parser.parse_args()

    MODEL_NAME = args.model
    GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

    active_skills = TEST_SKILLS
    if args.skill:
        active_skills = [s for s in TEST_SKILLS if s['id'] == args.skill]
        if not active_skills:
            print(f"Скилл '{args.skill}' не найден. Доступные: {[s['id'] for s in TEST_SKILLS]}")
            return

    print("=" * 70)
    print("LIVE E2E EVALUATION — Gemini API (Google AI Studio)")
    print(f"Тестируем {sum(len(s['tests']) for s in active_skills)} сценариев "
          f"по {len(active_skills)} скиллам")
    print("=" * 70)

    all_results = []
    total_tests = 0
    total_passed = 0

    for skill_cfg in active_skills:
        skill_id = skill_cfg['id']
        skill_content = load_skill(skill_id)
        if not skill_content:
            print(f"\n[SKIP] Скилл не найден: {skill_id}")
            continue

        print(f"\n{'─'*70}")
        print(f"СКИЛЛ: {skill_id}")
        print(f"{'─'*70}")

        skill_results = {'skill_id': skill_id, 'tests': []}

        for test in skill_cfg['tests']:
            test_type = test['type']
            user_prompt = test['user_prompt']
            total_tests += 1

            print(f"\n  [{test_type}]")
            print(f"  Промпт: {user_prompt[:80]}...")
            print(f"  Вызов Gemini API...", end='', flush=True)

            start = time.time()
            response = call_gemini(skill_content, user_prompt)
            elapsed = time.time() - start

            print(f" {elapsed:.1f}s")

            if response.startswith('[API ERROR') or response.startswith('[ERROR]'):
                print(f"  ❌ {response}")
                skill_results['tests'].append({
                    'type': test_type,
                    'prompt': user_prompt,
                    'response': response,
                    'passed': False,
                    'checks': [],
                    'elapsed': elapsed
                })
                continue

            passed, checks = judge_response(response, skill_id, test_type)
            total_passed += int(passed)

            # Вывод результатов
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"  {status}")
            for ch in checks:
                icon = "  ✓" if ch['passed'] else "  ✗"
                print(f"    {icon} {ch['check']}: {ch['detail']}")

            # Первые 400 символов ответа
            print(f"\n  Ответ (первые 400 симв):\n  {'─'*50}")
            preview = response[:400].replace('\n', '\n  ')
            print(f"  {preview}")
            if len(response) > 400:
                print(f"  ... [+{len(response)-400} символов]")

            skill_results['tests'].append({
                'type': test_type,
                'prompt': user_prompt,
                'response': response,
                'passed': passed,
                'checks': checks,
                'elapsed_s': round(elapsed, 2)
            })

            time.sleep(4)  # Rate limit pacing

        all_results.append(skill_results)

    # ─── Итоговый отчет ───────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"ИТОГИ LIVE E2E ТЕСТИРОВАНИЯ")
    print(f"{'='*70}")
    print(f"Всего тестов: {total_tests}")
    print(f"Пройдено:     {total_passed} ({total_passed/total_tests*100:.0f}%)")
    print(f"Провалено:    {total_tests - total_passed}")

    # Сохраняем полный отчет
    report_path = os.path.join(ROOT_DIR, f'live_eval_report_{MODEL_NAME.replace("/","_")}.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Live E2E Evaluation Report (Gemini API)\n\n")
        f.write(f"**Дата:** {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Модель:** {MODEL_NAME}\n")
        f.write(f"**Итог:** {total_passed}/{total_tests} тестов пройдено\n\n")
        f.write("---\n\n")

        for skill_data in all_results:
            f.write(f"## Скилл: `{skill_data['skill_id']}`\n\n")
            for t in skill_data['tests']:
                status = "PASSED" if t['passed'] else "FAILED"
                f.write(f"### {t['type']} — {status}\n\n")
                f.write(f"**Запрос:** {t['prompt']}\n\n")
                f.write(f"**Время ответа:** {t.get('elapsed_s', '?')}s\n\n")
                if 'checks' in t and t['checks']:
                    f.write("**Судейская оценка:**\n")
                    for ch in t['checks']:
                        icon = "✓" if ch['passed'] else "✗"
                        f.write(f"- {icon} {ch['check']}: {ch['detail']}\n")
                    f.write("\n")
                f.write("**Ответ модели:**\n")
                f.write(f"```markdown\n{t.get('response', '')[:2000]}\n```\n\n")
                f.write("---\n\n")

    print(f"\nПолный отчет сохранен: {report_path}")

if __name__ == '__main__':
    run_live_eval()
