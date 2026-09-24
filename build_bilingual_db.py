"""
Builds bilingual skills_db.js from all SKILL.md (RU) and SKILL.en.md (EN) files.
"""
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).parent.resolve()

def parse_skill_file(file_path):
    if not file_path.exists():
        return None
    content = file_path.read_text(encoding="utf-8")
    lines = content.replace("\r\n", "\n").split("\n")
    
    yaml_dict = {}
    in_yaml = False
    yaml_count = 0
    body_lines = []
    
    for l in lines:
        if l.strip() == "---":
            yaml_count += 1
            if yaml_count == 1:
                in_yaml = True
                continue
            elif yaml_count == 2:
                in_yaml = False
                continue
        if in_yaml:
            if ":" in l:
                k, v = l.split(":", 1)
                yaml_dict[k.strip()] = v.strip()
        else:
            if yaml_count >= 2:
                body_lines.append(l)
            else:
                body_lines.append(l)
                
    return {
        "name": yaml_dict.get("name", file_path.parent.name),
        "description": yaml_dict.get("description", ""),
        "preset": yaml_dict.get("preset", "core"),
        "content": content.strip()
    }

def build_db():
    source_dir = ROOT_DIR / "skills" if (ROOT_DIR / "skills").exists() and (ROOT_DIR / "skills").is_dir() else ROOT_DIR
    skill_dirs = sorted([d for d in source_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()])
    db = []
    
    for d in skill_dirs:
        ru_data = parse_skill_file(d / "SKILL.md")
        en_data = parse_skill_file(d / "SKILL.en.md") or ru_data
        
        entry = {
            "id": d.name,
            "preset": ru_data.get("preset", "core"),
            "ru": {
                "name": ru_data.get("name", d.name),
                "description": ru_data.get("description", ""),
                "content": ru_data.get("content", "")
            },
            "en": {
                "name": en_data.get("name", d.name),
                "description": en_data.get("description", ru_data.get("description", "")),
                "content": en_data.get("content", ru_data.get("content", ""))
            }
        }
        db.append(entry)
        
    js_content = "// Automatically generated bilingual database of 130 PM Skills (RU/EN)\n"
    js_content += "const SKILLS_DB = " + json.dumps(db, ensure_ascii=False, indent=2) + ";\n"
    
    (ROOT_DIR / "skills_db.js").write_text(js_content, encoding="utf-8")
    print(f"Successfully compiled bilingual skills_db.js with {len(db)} skills!")

if __name__ == "__main__":
    build_db()
