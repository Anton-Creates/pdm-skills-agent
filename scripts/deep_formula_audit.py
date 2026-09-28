import glob
import re
import os

latex_patterns = [
    r'\\[a-zA-Z]+',       # any \command like \frac, \times, \alpha, \text
    r'\$[^$\n]+\$',       # $...$
    r'\\\(.*?\\\)',       # \( ... \)
    r'\\\[.*?\\\]',       # \[ ... \]
    r'[\x00-\x08\x0b\x0c\x0e-\x1f]', # control chars
]

skills = glob.glob('skills/**/SKILL.md', recursive=True)
print(f"Total skills found: {len(skills)}")

issues = {}

for skill_path in sorted(skills):
    with open(skill_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    file_issues = []
    for line_num, line in enumerate(lines, 1):
        # Check control chars
        for m in re.finditer(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', line):
            file_issues.append((line_num, 'CONTROL_CHAR', repr(m.group(0)), line.strip()))
        
        # Check latex commands
        # Allow markdown escapes like \* or \_ or \[ if normal, but check for \alpha, \beta, \times, \frac, \text, etc.
        for m in re.finditer(r'\\(alpha|beta|gamma|delta|sigma|mu|lambda|theta|times|frac|text|ge|le|cdot|approx|rightarrow|sum|prod|sqrt|neq|pm|infty)', line):
            file_issues.append((line_num, 'LATEX_CMD', m.group(0), line.strip()))
            
        # Check $ ... $ math (exclude currency like $50M, $100, $1B, $5,000, etc.)
        dollar_matches = re.finditer(r'\$([^$\n]+)\$', line)
        for dm in dollar_matches:
            content = dm.group(1).strip()
            # If it's a currency like "$50k" or "$10M" or "$1,000" or "$X" in a list of dollar amounts
            if re.match(r'^\d+(\.\d+)?\s*(k|M|B|млн|тыс|руб|usd|\$|%)?$', content, re.IGNORECASE):
                continue
            # If it has math symbols or letters like H_0, H_1, alpha, beta, x, y, formula
            file_issues.append((line_num, 'DOLLAR_MATH', dm.group(0), line.strip()))

    if file_issues:
        issues[skill_path] = file_issues

print(f"\nFiles with potential issues: {len(issues)}")
for path, iss in issues.items():
    print(f"\n=== {path} ({len(iss)} issues) ===")
    for line_num, itype, val, line in iss:
        print(f"  Line {line_num} [{itype}]: {val}")
        print(f"    Text: {line[:120]}")
