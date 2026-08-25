import os, re

results = []
skill_dirs = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.') and os.path.exists(os.path.join(d, 'SKILL.md'))]
skill_dirs.sort()

for sd in skill_dirs:
    path = os.path.join(sd, 'SKILL.md')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fm_match = re.match(r'---\n(.*?)\n---', content, re.DOTALL)
    fm = {}
    if fm_match:
        for line in fm_match.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
    
    has_process = '## Процесс' in content or '## Process' in content
    has_rules = '## Правила' in content or '## Rules' in content or '## Guardrails' in content
    has_format = '## Формат' in content or '## Format' in content or '## Output' in content
    has_metrics_block = '### Универсальное правило метрики' in content
    
    rules_section = ''
    rules_match = re.search(r'## Правила\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not rules_match:
        rules_match = re.search(r'## Guardrails\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if rules_match:
        rules_section = rules_match.group(1).strip()
    rules_lines = [l for l in rules_section.split('\n') if l.strip().startswith('-')]
    
    fiveq_count = content.count('### Универсальное правило метрики')
    preset = fm.get('preset', '')
    allowed_tools = fm.get('allowed-tools', '')
    
    # Check if truly behavioral (has process + strong rules)
    behavioral = has_process and len(rules_lines) >= 4
    
    results.append({
        'id': sd,
        'preset': preset,
        'has_process': has_process,
        'has_rules': has_rules,
        'rules_count': len(rules_lines),
        'has_metrics_block': has_metrics_block,
        'allowed_tools': allowed_tools,
        'content_len': len(content),
        'fiveq_copies': fiveq_count,
        'behavioral': behavioral,
        'has_format': has_format,
    })

print(f'Total skills scanned: {len(results)}')
print()

print('=== NO PROCESS SECTION (pure templates) ===')
for r in results:
    if not r['has_process']:
        print(f"  {r['id']} ({r['preset']})")

print()
print('=== WEAK GUARDRAILS (<=2 rules or no rules) ===')
for r in results:
    if r['rules_count'] <= 2:
        print(f"  {r['id']} ({r['preset']}, rules={r['rules_count']})")

print()
print('=== STRONG BEHAVIORAL SKILLS (process + 4+ rules) ===')
for r in results:
    if r['behavioral']:
        print(f"  {r['id']} ({r['preset']}, rules={r['rules_count']})")

print()
total_5q = sum(r['fiveq_copies'] for r in results)
print(f'=== 5-QUESTION BLOCK: {total_5q} copies across {len(results)} skills ===')
print()

by_domain = {}
for r in results:
    p = r['preset']
    by_domain.setdefault(p, []).append(r)

print('=== DOMAIN SUMMARY ===')
for domain, skills in sorted(by_domain.items()):
    avg_rules = sum(s['rules_count'] for s in skills) / len(skills)
    pct_process = sum(1 for s in skills if s['has_process']) / len(skills) * 100
    pct_behavioral = sum(1 for s in skills if s['behavioral']) / len(skills) * 100
    print(f"  {domain}: {len(skills)} skills | avg_rules={avg_rules:.1f} | process={pct_process:.0f}% | behavioral={pct_behavioral:.0f}%")

print()
print('=== SHORT CONTENT (<2000 chars, likely thin) ===')
for r in sorted(results, key=lambda x: x['content_len']):
    if r['content_len'] < 2000:
        print(f"  {r['id']} ({r['preset']}): {r['content_len']} chars")
