#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_all_skills.py — Автономный E2E аудит всей библиотеки (130 скиллов)
Выполняется полностью автоматически:
- Загружает все 130 скиллов в 16 доменах.
- Генерирует реалистичный контекстный запрос для каждого скилла.
- Вызывает Gemini API (с автоматическим retry/backoff при 429 и паузами).
- Сохраняет результат каждого скилла в audit_checkpoint.json на лету.
- Вычисляет метрики глубины артефакта и взаимное семантическое перекрытие внутри домена.
- Формирует итоговый аналитический отчет SKILLS_AUDIT_REPORT.md с классификацией (KEEP / MERGE / DROP).
"""
import os
import sys
import json
import time
import re
import math
from collections import Counter, defaultdict
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CHECKPOINT_FILE = os.path.join(ROOT_DIR, 'audit_checkpoint.json')
REPORT_FILE = os.path.join(ROOT_DIR, 'SKILLS_AUDIT_REPORT.md')

# ─── 1. Загрузка конфигурации и API ключа ────────────────────────────────────
def load_env():
    env_path = os.path.join(ROOT_DIR, '.env')
    if not os.path.exists(env_path):
        print("[ERROR] Файл .env не найден")
        sys.exit(1)
    with open(env_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                k, v = line.split('=', 1)
                os.environ[k.strip()] = v.strip()

load_env()
API_KEY = os.environ.get('GEMINI_API_KEY', '')
if not API_KEY:
    print("[ERROR] GEMINI_API_KEY не задан в .env")
    sys.exit(1)

FALLBACK_MODELS = [
    "gemini-3.5-flash",
    "gemini-3.7-flash",
    "gemini-3.5-flash-lite",
    "gemini-3.1-pro-preview"
]
current_model_idx = 0

# ─── 2. Сбор и парсинг метаданных скиллов ────────────────────────────────────
def collect_all_skills():
    skills = []
    for entry in sorted(os.listdir(ROOT_DIR)):
        skill_path = os.path.join(ROOT_DIR, entry, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue
        try:
            content = open(skill_path, encoding='utf-8').read()
        except Exception:
            continue

        # Парсинг frontmatter
        fm_match = re.search(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        fm = {}
        if fm_match:
            for line in fm_match.group(1).splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    fm[k.strip()] = v.strip()

        preset = fm.get('preset', 'generic')
        desc = fm.get('description', '')
        hint = fm.get('argument-hint', '')
        name = fm.get('name', entry)

        # Очищенный промпт скилла без frontmatter
        clean_instructions = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

        skills.append({
            'id': entry,
            'name': name,
            'preset': preset,
            'desc': desc,
            'hint': hint,
            'instructions': clean_instructions
        })
    return skills

# ─── 3. Генератор реалистичных промптов ──────────────────────────────────────
DOMAIN_CONTEXTS = {
    'core': 'B2B SaaS платформа аналитики и трекинга задач',
    'discovery': 'Цифровой B2C маркетплейс локальных услуг и доставки',
    'growth': 'Финтех мобильное приложение необанка для физлиц',
    'saas': 'Облачная B2B платформа управления подписками и биллингом',
    'b2b': 'Enterprise CRM-система для корпоративных продаж и закупок',
    'internal-products': 'Корпоративный портал и HR-Tech SuperApp крупного ритейлера',
    'strategy': 'D2C омниканальный ритейлер электроники и товаров для дома',
    'platforms-tech': 'Highload инфраструктурная платформа микросервисов и API шлюзов',
    'fintech': 'Платежный шлюз и кредитный сервис для e-commerce покупателей',
    'marketplace': 'Двусторонний маркетплейс товаров с комиссионной моделью и доставкой',
    'e-commerce': 'Крупный интернет-магазин одежды и обуви с мобильным приложением',
    'retail-ops': 'Сеть дарксторов экспресс-доставки продуктов питания за 15 минут',
    'media-adtech': 'Рекламная сеть (DSP/SSP) и стриминговая контент-платформа',
    'edtech': 'Онлайн-университет профессионального образования и корпоративных курсов',
    'telecom': 'Федеральный телеком-оператор мобильной связи и цифровых VAS-сервисов',
    'govtech-b2g': 'Городской портал цифровых государственных услуг и суперсервисов'
}

def generate_user_prompt(skill):
    dom = skill['preset']
    base_ctx = DOMAIN_CONTEXTS.get(dom, 'Цифровой продукт')
    hint = re.sub(r'[\[\]]', '', skill['hint']).strip()
    if hint and len(hint) > 5:
        return f"Контекст: {base_ctx}. Задача: {hint}. Подготовь исчерпывающий продуктовый артефакт строго по процессу и структуре."
    else:
        return f"Контекст: {base_ctx}. Задача: Примени методику для инициативы развития продукта. Подготовь профессиональный артефакт."

# ─── 4. Вызов LLM с автоматическим retry и экспоненциальным backoff ──────────
def call_gemini(system_prompt, user_message, max_retries=10):
    global current_model_idx
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"СИСТЕМНАЯ ИНСТРУКЦИЯ СКИЛЛА:\n\n{system_prompt}\n\n---\n\nЗАПРОС ПОЛЬЗОВАТЕЛЯ:\n\n{user_message}"}]
            }
        ],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 4096,
        }
    }
    data = json.dumps(payload).encode('utf-8')
    last_error = '[API ERROR]: unknown'
    
    for attempt in range(max_retries + 1):
        model = FALLBACK_MODELS[current_model_idx]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
        req = urllib.request.Request(
            url,
            data=data,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                cand = result['candidates'][0]
                parts = cand['content'].get('parts', [])
                text = "".join([p.get('text', '') for p in parts if 'text' in p])
                return text
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8')
            last_error = f"[API ERROR {e.code}]: {body[:200]}"
            if e.code in (429, 503, 500):
                print(f" [{e.code} on {model}] -> Switching model... ", end='', flush=True)
                current_model_idx = (current_model_idx + 1) % len(FALLBACK_MODELS)
                time.sleep(5)
            elif attempt < max_retries:
                time.sleep(4)
            else:
                return last_error
        except Exception as ex:
            last_error = f"[ERROR on {FALLBACK_MODELS[current_model_idx]}]: {str(ex)}"
            if attempt < max_retries:
                time.sleep(3)
            else:
                return last_error
    return last_error

# ─── 5. Анализ текста и расчет метрик артефакта ──────────────────────────────
def evaluate_artifact(text):
    if not text or not isinstance(text, str) or text.startswith('[API ERROR') or text.startswith('[ERROR]') or not text.strip():
        return {
            'length': 0,
            'words': 0,
            'tables_count': 0,
            'metrics_count': 0,
            'has_process': False,
            'has_formulas': False,
            'score': 0,
            'valid': False
        }

    length = len(text)
    words = len(text.split())
    tables = len(re.findall(r'\|.*?\|.*?\|', text))
    metrics = len(re.findall(r'(\d+[\.,]?\d*\s*%|\$\s*\d+|\b\d+\s*(?:ms|мс|руб|чел|дней|спринт))', text, re.IGNORECASE))
    has_formulas = bool(re.search(r'(=|\+|-|\*|/|\\ge|\\le|≥|≤|CR|LTV|CAC|ROI|ARPU|NPS)', text))
    has_structure = bool(re.search(r'###?\s+[1-5]\.', text))

    # Скор качества артефакта (0 - 100)
    score = 0
    if length > 2000: score += 25
    elif length > 1200: score += 15
    if tables >= 2: score += 25
    elif tables >= 1: score += 15
    if metrics >= 5: score += 25
    elif metrics >= 2: score += 15
    if has_formulas: score += 15
    if has_structure: score += 10

    return {
        'length': length,
        'words': words,
        'tables_count': tables,
        'metrics_count': metrics,
        'has_structure': has_structure,
        'has_formulas': has_formulas,
        'score': min(score, 100),
        'valid': True
    }

# ─── 6. Расчет семантического перекрытия внутри домена ───────────────────────
def tokenize(text):
    words = re.findall(r'[a-zA-Zа-яА-ЯёЁ]{4,}', text.lower())
    stop_words = {'этот', 'быть', 'когда', 'если', 'чтобы', 'после', 'также', 'нужно', 'можно',
                  'команда', 'продукт', 'пользователь', 'процесс', 'система', 'данные', 'этап',
                  'метрика', 'результат', 'разработка', 'контекст', 'требования', 'релиз'}
    return [w for w in words if w not in stop_words]

def cosine_similarity(tokens1, tokens2):
    vec1 = Counter(tokens1)
    vec2 = Counter(tokens2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    if not denominator:
        return 0.0
    return float(numerator) / denominator

# ─── 7. Главный цикл аудита ──────────────────────────────────────────────────
def run_audit():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', help='Запустить аудит только для конкретного домена')
    parser.add_argument('--max', type=int, help='Максимальное количество скиллов для прогона')
    args = parser.parse_args()

    skills = collect_all_skills()
    if args.domain:
        skills = [s for s in skills if s['preset'] == args.domain]
    if args.max:
        skills = skills[:args.max]

    print("=" * 75)
    print(f"АВТОНОМНЫЙ E2E АУДИТ БИБЛИОТЕКИ SKILLS BUILDER ({len(skills)} СКИЛЛОВ)")
    print(f"Модели (Fallback): {', '.join(FALLBACK_MODELS)} | Чекпоинт: {os.path.basename(CHECKPOINT_FILE)}")

    print("=" * 75)

    # Загружаем уже имеющийся чекпоинт
    checkpoint = {}
    if os.path.exists(CHECKPOINT_FILE):
        try:
            checkpoint = json.load(open(CHECKPOINT_FILE, encoding='utf-8'))
            already_done = sum(1 for s in skills if s['id'] in checkpoint and checkpoint[s['id']].get('evaluated', False))
            print(f"[RESUME] В чекпоинте уже есть: {already_done}/{len(skills)} скиллов")
        except Exception:
            checkpoint = {}

    # 1. Прогон генерации для каждого скилла
    for idx, s in enumerate(skills, 1):
        sid = s['id']
        preset = s['preset']

        if sid in checkpoint and checkpoint[sid].get('evaluated', False):
            continue

        prompt = generate_user_prompt(s)
        print(f"[{idx:3d}/{len(skills)}] {preset:16} | {sid:28} ... ", end='', flush=True)

        start = time.time()
        resp = call_gemini(s['instructions'], prompt)
        elapsed = time.time() - start

        eval_res = evaluate_artifact(resp)
        tokens = tokenize(resp) if eval_res['valid'] else []

        checkpoint[sid] = {
            'id': sid,
            'preset': preset,
            'name': s['name'],
            'prompt': prompt,
            'response_snippet': resp[:600],
            'elapsed_s': round(elapsed, 2),
            'eval': eval_res,
            'tokens': tokens[:200],  # топ ключевых токенов для кластеризации
            'evaluated': eval_res['valid']
        }

        # Сохранение в чекпоинт на каждом шаге
        with open(CHECKPOINT_FILE, 'w', encoding='utf-8') as f:
            json.dump(checkpoint, f, ensure_ascii=False, indent=2)

        status_str = f"Score: {eval_res['score']}% ({eval_res['words']} words, {eval_res['tables_count']} tbls) [{elapsed:.1f}s]"
        if not eval_res['valid']:
            status_str = f"❌ FAILED [{resp[:60]}]"
        print(status_str)

        time.sleep(3)  # Пауза между запросами

    # 2. Межскилловый семантический анализ (поиск пар на слияние)
    print("\n" + "=" * 75)
    print("РАСЧЕТ ВЗАИМНОГО СЕМАНТИЧЕСКОГО ПЕРЕКРЫТИЯ (КАНДИДАТЫ НА СЛИЯНИЕ)...")
    print("=" * 75)

    domain_skills = defaultdict(list)
    for sid, data in checkpoint.items():
        if data.get('evaluated', False):
            domain_skills[data['preset']].append(data)

    high_overlap_pairs = []
    for preset, sk_list in domain_skills.items():
        n = len(sk_list)
        for i in range(n):
            for j in range(i + 1, n):
                s1 = sk_list[i]
                s2 = sk_list[j]
                sim = cosine_similarity(s1.get('tokens', []), s2.get('tokens', []))
                if sim >= 0.55:  # Высокое пересечение сгенерированных текстов
                    high_overlap_pairs.append({
                        'preset': preset,
                        'skill_1': s1['id'],
                        'skill_2': s2['id'],
                        'similarity': round(sim, 3),
                        'score_1': s1['eval']['score'],
                        'score_2': s2['eval']['score']
                    })

    high_overlap_pairs.sort(key=lambda x: x['similarity'], reverse=True)

    # 3. Формирование рекомендаций (Классификация)
    recommendations = {}
    for sid, data in checkpoint.items():
        ev = data.get('eval', {})
        score = ev.get('score', 0)
        length = ev.get('length', 0)

        # Проверка на наличие в парах дубликатов
        overlaps = [p for p in high_overlap_pairs if p['skill_1'] == sid or p['skill_2'] == sid]

        if not data.get('evaluated', False) or score < 40 or length < 800:
            status = '🔴 DROP / OVERHAUL'
            reason = 'Низкая глубина артефакта, отсутствие таблиц/метрик или тривиальный вывод'
        elif overlaps and overlaps[0]['similarity'] >= 0.65:
            partner = overlaps[0]['skill_2'] if overlaps[0]['skill_1'] == sid else overlaps[0]['skill_1']
            status = '🟡 MERGE CANDIDATE'
            reason = f'Высокое смысловое перекрытие ({int(overlaps[0]["similarity"]*100)}%) со скиллом `{partner}`'
        else:
            status = '🟢 KEEP (MUST-HAVE)'
            reason = 'Уникальная предметная ценность, сильные формулы и независимый артефакт'

        recommendations[sid] = {
            'preset': data.get('preset', ''),
            'name': data.get('name', sid),
            'status': status,
            'score': score,
            'reason': reason
        }

    # 4. Генерация итогового Markdown отчета
    generate_audit_report(checkpoint, high_overlap_pairs, recommendations)

def generate_audit_report(checkpoint, overlaps, recommendations):
    total = len(recommendations)
    keep_count = sum(1 for r in recommendations.values() if 'KEEP' in r['status'])
    merge_count = sum(1 for r in recommendations.values() if 'MERGE' in r['status'])
    drop_count = sum(1 for r in recommendations.values() if 'DROP' in r['status'])

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Итоговый отчет глобального E2E-аудита библиотеки PdM Skills Builder\n\n")
        f.write(f"**Дата аудита:** {time.strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Протестировано скиллов:** {total}\n")
        f.write(f"**Модели генерации:** {', '.join(FALLBACK_MODELS)}\n\n")

        f.write("## 1. Сводная матрица библиотеки\n\n")
        f.write(f"- 🟢 **Must-have (Оставить как золотой стандарт):** {keep_count} скиллов ({keep_count/total*100:.1f}%)\n")
        f.write(f"- 🟡 **Кандидаты на слияние (Merge Candidates):** {merge_count} скиллов ({merge_count/total*100:.1f}%)\n")
        f.write(f"- 🔴 **Кандидаты на удаление/переработку (Drop/Overhaul):** {drop_count} скиллов ({drop_count/total*100:.1f}%)\n\n")

        f.write("```text\n")
        target_size = keep_count + (merge_count // 2)
        f.write(f"РЕКОМЕНДОВАННАЯ ЦЕЛЕВАЯ СТРУКТУРА: сжатие с {total} до {target_size} компактных, бескомпромиссных скиллов\n")
        f.write("```\n\n")

        f.write("## 2. Топ пар с максимальным семантическим пересечением (Кандидаты на объединение)\n\n")
        f.write("| Домен | Скилл 1 | Скилл 2 | Сходство выводов | Рекомендация по объединению |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- |\n")
        seen_pairs = set()
        for p in overlaps[:30]:
            pair_key = tuple(sorted([p['skill_1'], p['skill_2']]))
            if pair_key in seen_pairs:
                continue
            seen_pairs.add(pair_key)
            sim_pct = int(p['similarity'] * 100)
            f.write(f"| `{p['preset']}` | `{p['skill_1']}` | `{p['skill_2']}` | **{sim_pct}%** | Объединить в единый мастер-скилл |\n")
        f.write("\n---\n\n")

        f.write("## 3. Полный реестр скиллов и вердикт по каждому\n\n")
        f.write("| Домен | Скилл | Скор качества | Вердикт | Обоснование |\n")
        f.write("| :--- | :--- | :---: | :--- | :--- |\n")
        for sid, r in sorted(recommendations.items(), key=lambda x: (x[1]['preset'], x[1]['status'])):
            f.write(f"| `{r['preset']}` | `{sid}` | {r['score']}% | {r['status']} | {r['reason']} |\n")

    print(f"\n[DONE] Итоговый отчет сохранен в {REPORT_FILE}")

if __name__ == '__main__':
    run_audit()
