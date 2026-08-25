#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
"""
PdM Skills Builder - Quality Test Suite
========================================
Запуск: python test_skills.py
Запуск по домену: python test_skills.py --domain core
Запуск по скиллу: python test_skills.py --skill prd
Только failed: python test_skills.py --failed-only
Вывод JSON:      python test_skills.py --json
"""

import os
import re
import sys
import json
import argparse
from dataclasses import dataclass, field
from typing import List, Optional

# ─── Конфигурация ────────────────────────────────────────────────────────────

VALID_PRESETS = {
    'core', 'discovery', 'growth', 'saas', 'b2b', 'internal-products',
    'strategy', 'platforms-tech', 'fintech', 'marketplace', 'e-commerce',
    'retail-ops', 'media-adtech', 'edtech', 'telecom', 'govtech-b2g'
}

VALID_LIFECYCLES = {'any', 'discovery', 'strategy', 'delivery', 'operations', 'strategy,operations'}
VALID_BUSINESS_MODELS = {'any', 'b2c', 'b2b', 'b2b2c', 'marketplace'}
VALID_STAGES = {'any', 'idea', 'mvp', 'pre-pmf', 'pmf', 'scale', 'concept',
                'idea,mvp,pre-pmf,pmf,scale', 'idea,mvp', 'mvp,pmf', 'pmf,scale'}
VALID_OUTPUT_ARTIFACTS = {'document', 'spec', 'analysis', 'plan', 'framework',
                           'product-tenets', 'canvas', 'checklist', 'strategy'}

REQUIRED_FM_FIELDS = ['name', 'description', 'argument-hint', 'allowed-tools',
                       'preset', 'lifecycle', 'business-model', 'stage', 'output-artifact']

FIVE_Q_SIGNATURE = 'Универсальное правило метрики'
MIN_DESCRIPTION_LENGTH = 60
MIN_RULES_FOR_BEHAVIORAL = 4
MIN_CONTENT_LENGTH = 1800  # chars (net of frontmatter and 5q block)

# Сигнатуры сильных guardrails (слова, которые говорят о реальных запретах)
GUARDRAIL_SIGNALS = [
    'запрет', 'нельзя', 'обязателен', 'обязательно', 'не используй',
    'не делай', 'не рекомендуй', 'не допускай', 'не принимай', 'требует',
    'без .* невозможно', 'kill switch', 'guardrail', 'не более', 'максимум',
    'если .* не ', 'должен содержать', 'запрещены', 'обязана', 'нет данных',
    'fallback', 'блокир'
]


# ─── Структуры данных ─────────────────────────────────────────────────────────

@dataclass
class TestResult:
    name: str
    passed: bool
    severity: str  # 'error' | 'warning' | 'info'
    message: str
    points: int = 0  # очки если passed, 0 если failed


@dataclass
class SkillReport:
    skill_id: str
    preset: str
    total_tests: int = 0
    passed: int = 0
    failed_errors: int = 0
    failed_warnings: int = 0
    score: int = 0
    max_score: int = 0
    tier: str = ''
    results: List[TestResult] = field(default_factory=list)

    def add(self, result: TestResult):
        self.results.append(result)
        self.total_tests += 1
        self.max_score += result.points
        if result.passed:
            self.passed += 1
            self.score += result.points
        else:
            if result.severity == 'error':
                self.failed_errors += 1
            else:
                self.failed_warnings += 1

    def grade(self) -> str:
        if self.max_score == 0:
            return 'F'
        pct = self.score / self.max_score * 100
        if pct >= 90:
            return 'A'
        if pct >= 75:
            return 'B'
        if pct >= 55:
            return 'C'
        if pct >= 35:
            return 'D'
        return 'F'

    def tier_label(self) -> str:
        g = self.grade()
        if g in ('A', 'B'):
            return 'Tier 1'
        if g == 'C':
            return 'Tier 2'
        return 'Tier 3'


# ─── Парсер скилла ────────────────────────────────────────────────────────────

def parse_skill(path: str) -> dict:
    """Парсит SKILL.md и возвращает структурированный словарь."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    fm = {}
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()

    # Секции
    def get_section(header: str) -> str:
        pattern = rf'## {re.escape(header)}\n(.*?)(?=\n## |\Z)'
        m = re.search(pattern, content, re.DOTALL)
        return m.group(1).strip() if m else ''

    rules_ru = get_section('Правила')
    rules_en = get_section('Rules') or get_section('Guardrails')
    rules = rules_ru or rules_en

    process_ru = get_section('Процесс')
    process_en = get_section('Process')
    process = process_ru or process_en

    fmt_ru = get_section('Формат вывода')
    fmt_en = get_section('Output Format') or get_section('Format')
    fmt = fmt_ru or fmt_en

    # Строки правил (начинающиеся с -)
    rule_lines = [l.strip() for l in rules.split('\n') if l.strip().startswith('-')]

    # Чистый контент (без frontmatter и 5q блока)
    clean = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    clean_no5q = re.sub(r'## Метрики.*', '', clean, flags=re.DOTALL)
    clean_no5q = re.sub(r'## Metrics.*', '', clean_no5q, flags=re.DOTALL)

    # Сигнатура 5q блока
    fiveq_count = content.count(FIVE_Q_SIGNATURE)

    # Строки процесса (нумерованные шаги)
    process_steps = re.findall(r'^\d+\.', process, re.MULTILINE)

    return {
        'content': content,
        'clean_content': clean_no5q,
        'frontmatter': fm,
        'rules': rules,
        'rule_lines': rule_lines,
        'process': process,
        'process_steps': process_steps,
        'format': fmt,
        'fiveq_count': fiveq_count,
        'has_process': bool(process.strip()),
        'has_rules': bool(rules.strip()),
        'has_format': bool(fmt.strip()),
        'content_length': len(clean_no5q),
        'total_length': len(content),
    }


# ─── Тестовые функции ─────────────────────────────────────────────────────────

def test_frontmatter_complete(skill: dict) -> List[TestResult]:
    """T1: Все обязательные поля frontmatter присутствуют."""
    results = []
    fm = skill['frontmatter']
    for field_name in REQUIRED_FM_FIELDS:
        present = field_name in fm and fm[field_name].strip()
        results.append(TestResult(
            name=f'frontmatter.{field_name}',
            passed=present,
            severity='error',
            message=f'Поле "{field_name}" отсутствует или пустое' if not present else f'OK: {fm.get(field_name, "")}',
            points=2
        ))
    return results


def test_frontmatter_values(skill: dict) -> List[TestResult]:
    """T2: Значения frontmatter из допустимого набора."""
    results = []
    fm = skill['frontmatter']

    preset = fm.get('preset', '')
    results.append(TestResult(
        name='frontmatter.preset_valid',
        passed=preset in VALID_PRESETS,
        severity='error',
        message=f'preset="{preset}" не входит в допустимый список ({sorted(VALID_PRESETS)})' if preset not in VALID_PRESETS else f'OK: {preset}',
        points=3
    ))

    desc = fm.get('description', '')
    results.append(TestResult(
        name='frontmatter.description_length',
        passed=len(desc) >= MIN_DESCRIPTION_LENGTH,
        severity='warning',
        message=f'Description слишком короткое ({len(desc)} chars, минимум {MIN_DESCRIPTION_LENGTH})' if len(desc) < MIN_DESCRIPTION_LENGTH else 'OK',
        points=2
    ))

    # argument-hint должен выглядеть как [hint]
    hint = fm.get('argument-hint', '')
    results.append(TestResult(
        name='frontmatter.argument_hint_format',
        passed=hint.startswith('[') and hint.endswith(']'),
        severity='warning',
        message=f'argument-hint должен быть в формате [текст], получили: {hint}',
        points=1
    ))

    name = fm.get('name', '')
    skill_dir = os.path.basename(os.path.dirname(skill.get('_path', '/unknown/unknown')))
    results.append(TestResult(
        name='frontmatter.name_matches_dir',
        passed=(name == skill_dir),
        severity='error',
        message=f'name="{name}" не совпадает с именем папки "{skill_dir}"',
        points=2
    ))

    return results


def test_has_process(skill: dict) -> List[TestResult]:
    """T3: Скилл имеет секцию Процесс с нумерованными шагами."""
    has = skill['has_process']
    steps = skill['process_steps']
    results = [
        TestResult(
            name='structure.has_process_section',
            passed=has,
            severity='error',
            message='Отсутствует секция ## Процесс — AI не знает алгоритм выполнения задачи' if not has else f'OK: {len(steps)} шагов',
            points=5
        )
    ]
    if has:
        results.append(TestResult(
            name='structure.process_has_steps',
            passed=len(steps) >= 3,
            severity='warning',
            message=f'В Процессе только {len(steps)} шагов (минимум 3)' if len(steps) < 3 else f'OK: {len(steps)} шагов',
            points=3
        ))
    return results


def test_has_format(skill: dict) -> List[TestResult]:
    """T4: Скилл имеет секцию с форматом вывода."""
    has = skill['has_format']
    return [TestResult(
        name='structure.has_format_section',
        passed=has,
        severity='warning',
        message='Отсутствует секция ## Формат вывода — AI будет генерировать произвольную структуру',
        points=4
    )]


def test_has_rules(skill: dict) -> List[TestResult]:
    """T5: Скилл имеет секцию Правила."""
    has = skill['has_rules']
    return [TestResult(
        name='structure.has_rules_section',
        passed=has,
        severity='error',
        message='Отсутствует секция ## Правила — нет guardrails против ошибок',
        points=5
    )]


def test_rules_quantity(skill: dict) -> List[TestResult]:
    """T6: Количество правил достаточно для behavioral скилла."""
    count = len(skill['rule_lines'])
    # Исключаем "пиши на русском" из счета
    real_rules = [r for r in skill['rule_lines']
                  if 'русском' not in r.lower() and 'russian' not in r.lower()]
    real_count = len(real_rules)

    results = [
        TestResult(
            name='rules.count_total',
            passed=count >= 2,
            severity='warning',
            message=f'Только {count} правил (минимум 2)',
            points=2
        ),
        TestResult(
            name='rules.count_behavioral',
            passed=real_count >= MIN_RULES_FOR_BEHAVIORAL,
            severity='warning',
            message=f'Только {real_count} предметных правил (без "пиши на русском"). Нужно >= {MIN_RULES_FOR_BEHAVIORAL} для behavioral скилла',
            points=6
        )
    ]
    return results


def test_guardrail_quality(skill: dict) -> List[TestResult]:
    """T7: Правила содержат реальные guardrails (запреты/обязательства), а не декларации."""
    rules_text = skill['rules'].lower()
    found_signals = [s for s in GUARDRAIL_SIGNALS if re.search(s, rules_text)]
    has_real_guardrails = len(found_signals) >= 2

    return [TestResult(
        name='rules.guardrail_quality',
        passed=has_real_guardrails,
        severity='warning',
        message=f'Правила не содержат реальных guardrails (запретов/обязательств). Найдено сигналов: {found_signals}' if not has_real_guardrails else f'OK: найдено {len(found_signals)} guardrail-сигналов',
        points=5
    )]


def test_no_lang_only_rule(skill: dict) -> List[TestResult]:
    """T8: Единственное правило — не 'пиши на русском'."""
    rules = skill['rule_lines']
    only_lang = (len(rules) == 1 and 'русском' in rules[0].lower())

    return [TestResult(
        name='rules.not_only_language',
        passed=not only_lang,
        severity='error',
        message='"Пиши на русском" — единственное правило. Это языковая настройка, а не guardrail скилла.',
        points=5
    )]


def test_content_length(skill: dict) -> List[TestResult]:
    """T9: Скилл имеет достаточный объем контента."""
    length = skill['content_length']
    return [TestResult(
        name='content.net_length',
        passed=length >= MIN_CONTENT_LENGTH,
        severity='warning',
        message=f'Слишком мало контента: {length} символов (без frontmatter и 5q блока). Минимум {MIN_CONTENT_LENGTH}.',
        points=4
    )]


def test_fiveq_duplication(skill: dict) -> List[TestResult]:
    """T10: Блок '5 вопросов метрики' не дублируется внутри одного файла."""
    count = skill['fiveq_count']
    return [TestResult(
        name='content.no_5q_duplication',
        passed=count <= 1,
        severity='warning',
        message=f'Блок "5 вопросов" встречается {count} раза в одном файле',
        points=1
    )]


def test_section_order(skill: dict) -> List[TestResult]:
    """T11: Секции идут в правильном порядке (Процесс → Формат → Правила)."""
    content = skill['content']

    pos_process = content.find('## Процесс')
    if pos_process == -1:
        pos_process = content.find('## Process')

    pos_format = content.find('## Формат')
    if pos_format == -1:
        pos_format = content.find('## Output Format')

    pos_rules = content.find('## Правила')
    if pos_rules == -1:
        pos_rules = content.find('## Rules')
    if pos_rules == -1:
        pos_rules = content.find('## Guardrails')

    pos_metrics = content.find('## Метрики')
    if pos_metrics == -1:
        pos_metrics = content.find('## Metrics')

    results = []

    # Метрики не должны быть перед основным контентом
    main_heading_pos = content.find('\n# ')  # первый H1 после frontmatter
    if pos_metrics != -1 and main_heading_pos != -1:
        metrics_before_main = pos_metrics < main_heading_pos
        results.append(TestResult(
            name='structure.metrics_not_before_content',
            passed=not metrics_before_main,
            severity='error',
            message='Блок ## Метрики стоит ДО основного заголовка скилла — структурный баг (перепутан порядок секций)',
            points=3
        ))

    # Правила должны быть после Процесса
    if pos_process != -1 and pos_rules != -1:
        results.append(TestResult(
            name='structure.rules_after_process',
            passed=pos_rules > pos_process,
            severity='warning',
            message='Секция ## Правила стоит ДО ## Процесс',
            points=2
        ))

    return results


def test_examples_follow_own_rules(skill: dict) -> List[TestResult]:
    """T12: Если скилл требует 5 вопросов для метрик, примеры в Format тоже должны их соблюдать."""
    rules = skill['rules']
    fmt = skill['format']
    results = []

    requires_5q = '5 вопрос' in rules.lower() or 'правило метрик' in rules.lower()
    has_metrics_in_format = re.search(r'\b(Rate|Метрик|Conversion|Share|Ratio|Churn|Retention)\b', fmt, re.IGNORECASE)

    if requires_5q and has_metrics_in_format:
        # Проверяем что в Format есть хотя бы намек на ответы на 5 вопросов
        has_5q_answer = any(phrase in fmt for phrase in [
            'Кто владеет', 'Как часто', 'Какие события', 'Какой порог',
            'Owner', 'Frequency', 'Threshold', 'накрутить'
        ])
        results.append(TestResult(
            name='consistency.examples_follow_metrics_rule',
            passed=has_5q_answer,
            severity='warning',
            message='Скилл требует 5 вопросов для метрик, но примеры в "Формат вывода" сами не отвечают на эти вопросы — нарушение собственного правила',
            points=3
        ))

    return results


def test_format_has_template(skill: dict) -> List[TestResult]:
    """T13: Формат содержит реальный шаблон, а не только описание."""
    fmt = skill['format']
    if not fmt:
        return []

    # Настоящий шаблон содержит плейсхолдеры вроде [текст] или колонки таблицы
    has_placeholders = bool(re.search(r'\[.{3,50}\]|\|.*\|.*\|', fmt))

    return [TestResult(
        name='format.has_real_template',
        passed=has_placeholders,
        severity='warning',
        message='Раздел "Формат вывода" не содержит шаблон с плейсхолдерами — AI может произвольно интерпретировать структуру',
        points=3
    )]


def test_process_has_save_step(skill: dict) -> List[TestResult]:
    """T14: Процесс содержит шаг сохранения/экспорта артефакта."""
    process = skill['process']
    if not process:
        return []

    has_save = bool(re.search(r'сохран|export|write|save|вывод.*файл', process, re.IGNORECASE))

    return [TestResult(
        name='process.has_save_step',
        passed=has_save,
        severity='info',
        message='В Процессе нет явного шага сохранения результата в файл',
        points=1
    )]


def test_description_not_generic(skill: dict) -> List[TestResult]:
    """T15: Description не является обобщенным шаблоном."""
    desc = skill['frontmatter'].get('description', '')
    generic_phrases = [
        'проектировать продуктовые требования к',  # шаблонный
        'спецификация для',                          # шаблонный
    ]
    is_generic = any(p in desc.lower() for p in generic_phrases)
    # Для этого теста мягкий критерий — просто info
    return [TestResult(
        name='content.description_specific',
        passed=not is_generic or len(desc) > 120,  # длинный description — обычно нормальный
        severity='info',
        message='Description выглядит как шаблонная фраза — добавь специфику и уникальные guardrails',
        points=1
    )]


# ─── Движок запуска тестов ────────────────────────────────────────────────────

ALL_TEST_FUNCTIONS = [
    test_frontmatter_complete,
    test_frontmatter_values,
    test_has_process,
    test_has_format,
    test_has_rules,
    test_rules_quantity,
    test_guardrail_quality,
    test_no_lang_only_rule,
    test_content_length,
    test_fiveq_duplication,
    test_section_order,
    test_examples_follow_own_rules,
    test_format_has_template,
    test_process_has_save_step,
    test_description_not_generic,
]


def run_skill_tests(skill_dir: str) -> Optional[SkillReport]:
    """Запускает все тесты для одного скилла."""
    skill_path = os.path.join(skill_dir, 'SKILL.md')
    if not os.path.exists(skill_path):
        return None

    try:
        skill = parse_skill(skill_path)
        skill['_path'] = skill_path
    except Exception as e:
        print(f'  [ERROR] Не удалось распарсить {skill_path}: {e}')
        return None

    fm = skill['frontmatter']
    report = SkillReport(
        skill_id=os.path.basename(skill_dir),
        preset=fm.get('preset', 'unknown')
    )

    for test_fn in ALL_TEST_FUNCTIONS:
        try:
            results = test_fn(skill)
            for r in results:
                report.add(r)
        except Exception as e:
            report.add(TestResult(
                name=f'{test_fn.__name__}.exception',
                passed=False,
                severity='error',
                message=f'Ошибка при выполнении теста: {e}',
                points=0
            ))

    report.tier = report.tier_label()
    return report


# ─── Форматирование вывода ────────────────────────────────────────────────────

GRADE_COLORS = {
    'A': '\033[92m',  # green
    'B': '\033[96m',  # cyan
    'C': '\033[93m',  # yellow
    'D': '\033[91m',  # red
    'F': '\033[91m',  # red
}
RESET = '\033[0m'
BOLD = '\033[1m'


def color_grade(grade: str) -> str:
    return f"{GRADE_COLORS.get(grade, '')}{BOLD}{grade}{RESET}"


def format_report(report: SkillReport, failed_only: bool = False, verbose: bool = False) -> str:
    lines = []
    grade = report.grade()
    pct = int(report.score / report.max_score * 100) if report.max_score else 0

    lines.append(
        f"\n{BOLD}[{report.skill_id}]{RESET} "
        f"({report.preset}) "
        f"Grade: {color_grade(grade)} "
        f"{report.score}/{report.max_score} ({pct}%) | "
        f"Tier: {report.tier} | "
        f"Errors: {report.failed_errors} | Warnings: {report.failed_warnings}"
    )

    for r in report.results:
        if failed_only and r.passed:
            continue
        if not verbose and r.passed:
            continue
        icon = 'OK' if r.passed else ('ERR' if r.severity == 'error' else 'WARN')
        color = '\033[92m' if r.passed else ('\033[91m' if r.severity == 'error' else '\033[93m')
        lines.append(f"  {color}[{icon}]{RESET} [{r.name}] {r.message}")

    return '\n'.join(lines)


def print_summary(reports: List[SkillReport]):
    """Итоговая сводка по всем скиллам."""
    total = len(reports)
    grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    tiers = {'Tier 1': 0, 'Tier 2': 0, 'Tier 3': 0}
    total_errors = 0
    total_warnings = 0

    for r in reports:
        grades[r.grade()] += 1
        tiers[r.tier] += 1
        total_errors += r.failed_errors
        total_warnings += r.failed_warnings

    avg_score = sum(r.score for r in reports) / sum(r.max_score for r in reports) * 100 if reports else 0

    print(f"\n{'='*60}")
    print(f"{BOLD}ИТОГОВАЯ СВОДКА: {total} скиллов{RESET}")
    print(f"{'='*60}")
    print(f"Средний балл: {avg_score:.1f}%")
    print()
    print("Оценки:")
    for g, count in sorted(grades.items()):
        bar = '█' * count
        print(f"  {color_grade(g)}: {count:3d} {bar}")

    print()
    print("Tier-распределение:")
    for tier, count in sorted(tiers.items()):
        pct = count / total * 100 if total else 0
        print(f"  {tier}: {count} ({pct:.0f}%)")

    print()
    print(f"Всего ошибок (error):   {total_errors}")
    print(f"Всего предупреждений:   {total_warnings}")

    # Топ проблем
    problem_counts = {}
    for r in reports:
        for t in r.results:
            if not t.passed:
                problem_counts[t.name] = problem_counts.get(t.name, 0) + 1

    print()
    print("Топ-10 проблем по скиллам:")
    for name, count in sorted(problem_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  {count:3d}x  {name}")

    # Сводка по доменам
    domain_stats = {}
    for r in reports:
        p = r.preset
        if p not in domain_stats:
            domain_stats[p] = {'reports': []}
        domain_stats[p]['reports'].append(r)

    print()
    print("Средний балл по доменам:")
    for domain, stats in sorted(domain_stats.items()):
        reps = stats['reports']
        avg = sum(r.score for r in reps) / sum(r.max_score for r in reps) * 100 if reps else 0
        t1 = sum(1 for r in reps if r.tier == 'Tier 1')
        print(f"  {domain:20s}: {avg:5.1f}% | Tier1={t1}/{len(reps)}")


# ─── Точка входа ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='PdM Skills Quality Test Suite')
    parser.add_argument('--domain', help='Фильтр по домену (preset)')
    parser.add_argument('--skill', help='Проверить один конкретный скилл')
    parser.add_argument('--failed-only', action='store_true', help='Показывать только провалившиеся тесты')
    parser.add_argument('--verbose', action='store_true', help='Показывать все тесты, включая пройденные')
    parser.add_argument('--json', action='store_true', help='Вывод в JSON формате')
    parser.add_argument('--min-grade', choices=['A', 'B', 'C', 'D', 'F'], help='Показывать только скиллы хуже указанной оценки')
    args = parser.parse_args()

    # Определяем рабочую директорию
    base_dir = os.path.dirname(os.path.abspath(__file__))

    if args.skill:
        skill_dirs = [os.path.join(base_dir, args.skill)]
    else:
        skill_dirs = [
            os.path.join(base_dir, d) for d in sorted(os.listdir(base_dir))
            if os.path.isdir(os.path.join(base_dir, d))
            and not d.startswith('.')
            and os.path.exists(os.path.join(base_dir, d, 'SKILL.md'))
        ]

    reports = []
    for skill_dir in skill_dirs:
        report = run_skill_tests(skill_dir)
        if report is None:
            continue

        # Фильтр по домену
        if args.domain and report.preset != args.domain:
            continue

        reports.append(report)

    if args.json:
        output = []
        for r in reports:
            output.append({
                'skill_id': r.skill_id,
                'preset': r.preset,
                'grade': r.grade(),
                'tier': r.tier,
                'score': r.score,
                'max_score': r.max_score,
                'pct': round(r.score / r.max_score * 100, 1) if r.max_score else 0,
                'failed_errors': r.failed_errors,
                'failed_warnings': r.failed_warnings,
                'failures': [
                    {'name': t.name, 'severity': t.severity, 'message': t.message}
                    for t in r.results if not t.passed
                ]
            })
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # Фильтр по минимальной оценке
    grade_order = ['A', 'B', 'C', 'D', 'F']
    if args.min_grade:
        min_idx = grade_order.index(args.min_grade)
        reports_to_show = [r for r in reports if grade_order.index(r.grade()) >= min_idx]
    else:
        reports_to_show = reports

    for report in reports_to_show:
        print(format_report(report, failed_only=args.failed_only, verbose=args.verbose))

    print_summary(reports)


if __name__ == '__main__':
    main()
