#!/usr/bin/env python3
import os
import re
from pathlib import Path
from collections import OrderedDict

REPO_ROOT = Path(__file__).resolve().parent.parent
PY_DIR = REPO_ROOT / "Python"
JAVA_DIR = REPO_ROOT / "Java"
DOCS_FILE = REPO_ROOT / "docs" / "problems_list.md"
README_FILE = REPO_ROOT / "README.md"

def extract_meta(path: Path):
    title = None
    link = None
    difficulty = ""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line in enumerate(f):
                if i > 40:
                    break
                # LeetCode: Title
                m = re.search(r'LeetCode\s*[:\-]\s*(.+)', line, re.I)
                if m and not title:
                    title = m.group(1).strip()
                m2 = re.search(r'Link\s*[:\-]\s*(https?://\S+)', line, re.I)
                if m2 and not link:
                    link = m2.group(1).strip().rstrip(').,')
                m3 = re.search(r'Difficulty\s*[:\-]\s*(\w+)', line, re.I)
                if m3 and not difficulty:
                    difficulty = m3.group(1).strip().title()
    except Exception:
        pass

    if not title:
        # derive from filename
        name = path.stem
        name = re.sub(r'^\d+[_\-\s]*', '', name)
        title = name.replace('_', ' ').replace('-', ' ').title()
    return title, link, difficulty

def scan():
    problems = OrderedDict()  # key -> {title, link, difficulty, langs}
    for lang, base in (("Python", PY_DIR), ("Java", JAVA_DIR)):
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.*")):
            if p.suffix.lower() not in (".py", ".java"):
                continue
            title, link, difficulty = extract_meta(p)
            key = link if link else title
            if key not in problems:
                problems[key] = {"title": title, "link": link, "difficulty": difficulty, "langs": set()}
            problems[key]["langs"].add(lang)
            # prefer to keep non-empty difficulty
            if not problems[key]["difficulty"] and difficulty:
                problems[key]["difficulty"] = difficulty
    return problems

def write_docs(problems):
    lines = []
    lines.append("# Problems List\n")
    lines.append("Automatically generated. Solutions are in the `Python/` and `Java/` directories.\n")
    lines.append("| # | Problem | Difficulty | Python | Java |")
    lines.append("|---|---|---:|:---:|:---:|")
    idx = 1
    for key, entry in problems.items():
        title = entry["title"]
        link = entry["link"]
        diff = entry["difficulty"] or ""
        py = "✅" if "Python" in entry["langs"] else ""
        java = "✅" if "Java" in entry["langs"] else ""
        if link:
            problem_md = f"[{title}]({link})"
        else:
            problem_md = title
        lines.append(f"| {idx} | {problem_md} | {diff} | {py} | {java} |")
        idx += 1
    DOCS_FILE.parent.mkdir(parents=True, exist_ok=True)
    DOCS_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {DOCS_FILE}")

def update_readme(problems):
    if not README_FILE.exists():
        print("README.md not found; skipping README update")
        return
    content = README_FILE.read_text(encoding="utf-8")
    start = "<!-- PROGRESS_TABLE_START -->"
    end = "<!-- PROGRESS_TABLE_END -->"
    if start in content and end in content:
        summary = f"\nGenerated: **{len(problems)}** problems. See `docs/problems_list.md` for details.\n\n"
        new_content = content.split(start)[0] + start + "\n" + summary + end + content.split(end)[1]
        README_FILE.write_text(new_content, encoding="utf-8")
        print("Updated README.md between markers")
    else:
        print("Markers not found in README.md; please add <!-- PROGRESS_TABLE_START --> and <!-- PROGRESS_TABLE_END -->")

def main():
    problems = scan()
    write_docs(problems)
    update_readme(problems)

if __name__ == "__main__":
    main()
