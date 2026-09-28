import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('skills_db.js', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('[')
end = text.rfind(']')
skills = json.loads(text[start:end+1])

print(f"Auditing {len(skills)} skills in skills_db.js...")

issues = []
for s in skills:
    for lang in ['ru', 'en']:
        c = s[lang]['content']
        # 1. LaTeX commands
        bad_latex = re.findall(r'\\(alpha|beta|gamma|delta|sigma|mu|lambda|theta|times|frac|text|ge|le|cdot|approx|rightarrow|sum|prod|sqrt|neq|pm|infty)', c)
        if bad_latex:
            issues.append((s['id'], lang, "LATEX", str(set(bad_latex))))
            
        # 2. Control chars
        control = re.findall(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', c)
        if control:
            issues.append((s['id'], lang, "CONTROL_CHAR", str([hex(ord(ch)) for ch in control])))
            
        # 3. Dollar math with mathematical symbols
        dollars = re.finditer(r'\$([^$\n]+)\$', c)
        for dm in dollars:
            val = dm.group(1).strip()
            # If it's a pure currency or price range (e.g. $100, $50k, $0.30, $29)
            if re.match(r'^\d+(\.\d+)?\s*(k|m|b|млн|тыс|usd|руб|\$|%|мес|/мес|/mo|per month)?$', val, re.I):
                continue
            # If it contains math operators or subscripts
            if any(op in val for op in ['=', '+', '-', '*', '/', '_', '^', '<', '>', '≤', '≥', 'β', 'α', 'χ']):
                # Ignore currency combinations like "$0.30 за транзакцию" or "2.9% + $0.30"
                if re.search(r'\d+(\.\d+)?\s*(за|per|мес|год)', val, re.I):
                    continue
                issues.append((s['id'], lang, "DOLLAR_MATH", val))

print(f"\nTotal issues found: {len(issues)}")
for sid, lang, itype, desc in issues:
    print(f"  [{sid}] ({lang}) [{itype}]: {desc}")
