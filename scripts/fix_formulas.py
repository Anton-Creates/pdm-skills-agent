"""
Script to audit and fix broken LaTeX / TeX escape sequences across all 130 skills.
Replaces raw LaTeX with clean, universal Unicode mathematical symbols.
"""
import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def clean_skill_content(text):
    # 1. Search ranking broken table rows due to \r / \rightarrow
    text = re.sub(r'\[`"айфон 15 про маккс"`\s*\$\s*\n\s*ightarrow\$\s*`"iphone 15 pro max"`\]', '[`"айфон 15 про маккс"` → `"iphone 15 pro max"`]', text)
    text = re.sub(r'\[`"купить кроссовки"`\s*\$\s*\n\s*ightarrow\$\s*Категория: Обувь/Спорт\]', '[`"купить кроссовки"` → Категория: Обувь/Спорт]', text)
    text = re.sub(r'\[`"сотовый телефон"`\s*\$\s*\n\s*ightarrow\$\s*`"смартфон"`, `\"мобильный\"`\]', '[`"сотовый телефон"` → `"смартфон"`, `"мобильный"`]', text)
    text = re.sub(r'\[`"сотовый телефон"`\s*\$\s*\n\s*ightarrow\$\s*`"смартфон"`, `"мобильный"`\]', '[`"сотовый телефон"` → `"смартфон"`, `"мобильный"`]', text)
    text = re.sub(r'\$ightarrow\$', '→', text)
    text = re.sub(r'\\rightarrow', '→', text)

    # 2. Specific complex formulas
    # Demand forecasting
    text = re.sub(r'\$Z\s*(?:\\times|\t?imes)\s*\\sigma_\{?\\text\{demand\}\}?\s*(?:\\times|\t?imes)\s*\\sqrt\{\\text\{LeadTime\}\}\$', 'Z × σ_demand × √(LeadTime)', text)
    text = re.sub(r'\$\(\\text\{Спрос\}\s*(?:\\times|\t?imes)\s*\\text\{LeadTime\}\)\s*\+\s*\\text\{SafetyStock\}\$', '(Спрос × LeadTime) + SafetyStock', text)
    text = re.sub(r'\$\\frac\{\\sum\s*\|Fact\s*-\s*Forecast\|\}\{\\sum\s*Fact\}\$', 'Σ|Fact − Forecast| / Σ(Fact)', text)
    text = re.sub(r'\$\\frac\{\\sum\s*\(Forecast\s*-\s*Fact\)\}\{\\sum\s*Fact\}\$', 'Σ(Forecast − Fact) / Σ(Fact)', text)

    # SaaS metrics
    text = re.sub(r'\$\\frac\{\\text\{Starting\}\s*\+\s*\\text\{Expansion\}\s*-\s*\\text\{Contraction\}\s*-\s*\\text\{Churn\}\}\{\\text\{Starting\}\}\$', '(Starting + Expansion − Contraction − Churn) / Starting', text)
    text = re.sub(r'\$\\frac\{\\text\{New MRR\}\s*\+\s*\\text\{Expansion MRR\}\}\{\\text\{Contraction MRR\}\s*\+\s*\\text\{Churned MRR\}\}\$', '(New MRR + Expansion MRR) / (Contraction MRR + Churned MRR)', text)
    text = re.sub(r'\$\\frac\{\\text\{Quarterly Net New ARR\}\s*(?:\\times|\t?imes)\s*4\}\{\\text\{S&M Expense\}\}\$', '(Quarterly Net New ARR × 4) / S&M Expense', text)

    # Other domain formulas
    text = re.sub(r'\$\\text\{Incremental Lift\}\s*=\s*\\text\{Выручка тестовой группы\}\s*-\s*\\text\{Выручка контрольной группы\}\$', 'Incremental Lift = Выручка тестовой группы − Выручка контрольной группы', text)
    text = re.sub(r'\$\\text\{Выручка\}\s*=\s*\\text\{Активные покупатели\}\s*(?:\\times|\t?imes)\s*\\text\{Частота заказов\}\s*(?:\\times|\t?imes)\s*\\text\{Средний чек\}\$', 'Выручка = Активные покупатели × Частота заказов × Средний чек', text)
    text = re.sub(r'\$\(\\text\{Стоимость очного\}\s*-\s*\\text\{Стоимость цифрового\}\)\s*(?:\\times|\t?imes)\s*\\text\{Объем электронных заявлений\}\$', '(Стоимость очного − Стоимость цифрового) × Объем электронных заявлений', text)
    text = re.sub(r'\$\\text\{Cost per Ticket\}\s*=\s*\\frac\{\\text\{ФОТ линии поддержки\}\s*\+\s*\\text\{Стоимость лицензий ITSM\}\}\{\\text\{Общее количество закрытых тикетов за месяц\}\}\$', 'Cost per Ticket = (ФОТ линии поддержки + Стоимость ITSM) / Количество закрытых тикетов', text)
    text = re.sub(r'\$\\min\s*\\sum\s*\\text\{ETA\}_\{ij\}\s*\+\s*\\text\{Surge Penalty\}\$', 'min Σ(ETA_ij) + Surge Penalty', text)

    # 3. Growth loop
    text = re.sub(r'\$K\s*=\s*i\s*(?:\\times|\t?imes)\s*c\$', 'K = i × c', text)
    text = re.sub(r'\$T_\{?\\text\{cycle\}\}?\b\$?', 'T_cycle', text)
    text = re.sub(r'\bT_cycle\$', 'T_cycle', text)
    text = re.sub(r'\$K\s*<\s*0\.2\$', 'K < 0.2', text)

    # 4. Search ranking variables
    text = re.sub(r'\$S_\{?\\text\{text\}\}?\b\$?', 'S_text', text)
    text = re.sub(r'\$S_\{?\\text\{CR\}\}?\b\$?', 'S_CR', text)
    text = re.sub(r'\$S_\{?\\text\{log\}\}?\b\$?', 'S_log', text)
    text = re.sub(r'\$S_\{?\\text\{price\}\}?\b\$?', 'S_price', text)
    text = re.sub(r'\$S_\{?\\text\{rep\}\}?\b\$?', 'S_rep', text)
    text = re.sub(r'\b(S_text|S_CR|S_log|S_price|S_rep)\$', r'\1', text)
    text = re.sub(r'Рейтинг\s*\$≥\s*4\.5\$,\s*% брака\s*\$<\s*1%\$', 'Рейтинг ≥ 4.5, % брака < 1%', text)

    # 5. Matching algorithm surge
    text = re.sub(r'\[Спрос\s*\$1\.1\s*-\s*1\.5\s*×\$\s*Предложения\]', '[Спрос 1.1 - 1.5× Предложения]', text)

    # 6. Statistics / A/B testing
    text = re.sub(r'\$H_0\$', 'H₀', text)
    text = re.sub(r'\$H_1\$', 'H₁', text)
    text = re.sub(r'\$1\s*-\s*\\?beta\s*=\s*80\\?%\$', '1 - β = 80%', text)
    text = re.sub(r'\$1\s*-\s*\\?beta\s*=\s*0\.80\$', '1 - β = 0.80', text)
    text = re.sub(r'\$1\s*-\s*\\?beta\$', '1 - β', text)
    text = re.sub(r'\$\\?alpha\s*=\s*0\.05\$', 'α = 0.05', text)
    text = re.sub(r'\$\\?alpha\s*=\s*0\.05,\s*\\?beta\s*=\s*0\.20\$', 'α = 0.05, β = 0.20', text)
    text = re.sub(r'\$\\?chi\^2\$', 'χ²', text)
    text = re.sub(r'\$p\\?text\{-value\}\s*<\s*0\.001\$', 'p-value < 0.001', text)
    text = re.sub(r'\$p\s*<\s*0\.05\$', 'p < 0.05', text)
    text = re.sub(r'\$p\s*<\s*0\.001\$', 'p < 0.001', text)
    text = re.sub(r'SRM\s*\$p\s*<\s*0\.001\$', 'SRM p < 0.001', text)
    text = re.sub(r'Target:\s*\$p\s*<\s*0\.05\$', 'Target: p < 0.05', text)

    # 7. TeX tokens inside text
    text = re.sub(r'\\ge', '≥', text)
    text = re.sub(r'\\le', '≤', text)
    text = re.sub(r'\\pm', '±', text)
    text = re.sub(r'\\times', '×', text)
    text = text.replace('\t' + 'imes', '×')
    text = re.sub(r'\\%', '%', text)
    text = re.sub(r'\+2\^\\?circ\\?text\{C\}', '+2°C', text)
    text = re.sub(r'\+4\^\\?circ\\?text\{C\}', '+4°C', text)
    text = re.sub(r'>\s*\+6\^\\?circ\\?text\{C\}', '> +6°C', text)
    text = re.sub(r'\\text\{([^}]+)\}', r'\1', text)

    # 8. Unwrap remaining simple math expressions wrapped in $...$
    def unwrap_dollar(m):
        inner = m.group(1).strip()
        # Do not touch dollar currency like '$0.30' or '$29 до $39'
        if any(inner.startswith(prefix) for prefix in ['≥', '≤', '±', '>', '<', '+', '-', '×', 'min', 'Σ']) \
           or any(inner.endswith(suffix) for suffix in ['%', 'x', 'px', 'pt', 'M', 'C', '°C', ':1']) \
           or inner in ['K', 'i', 'c', '1.0x', '1.5x', '0.8x', '3x', '2x', '1x', '0.5x', '0.25x', 'H_0', 'H_1', 'H₀', 'H₁', '1-β', '1 - β', 'α', 'β', 'χ²'] \
           or re.match(r'^\d+(\.\d+)?%$', inner) \
           or re.match(r'^\d+-\d+%$', inner) \
           or re.match(r'^\d+/\d+$', inner) \
           or re.match(r'^\d+\.\d+\s*/\s*\d+\.\d+$', inner):
            return inner
        return m.group(0)

    text = re.sub(r'\$([^$\n]+)\$', unwrap_dollar, text)
    return text

def run_fix():
    skills_dir = ROOT_DIR / "skills"
    md_files = sorted(list(skills_dir.glob("**/*.md")))
    changed_count = 0

    for path in md_files:
        original = path.read_text(encoding="utf-8")
        cleaned = clean_skill_content(original)
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            changed_count += 1
            print(f"Fixed formulas in: {path.relative_to(ROOT_DIR)}")

    print(f"\nCompleted! Fixed formulas in {changed_count} files.")

if __name__ == "__main__":
    run_fix()
