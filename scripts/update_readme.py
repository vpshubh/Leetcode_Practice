import os
import re

README_FILE = "README.md"
PROBLEMS_LIST_FILE = "docs/problems_list.md"
START_MARKER = "<!-- PROGRESS_TABLE_START -->"
END_MARKER = "<!-- PROGRESS_TABLE_END -->"
SOLVED_LOG = "solved_problems.txt"

SOLUTION_FOLDERS = [
    "Python/easy", "Python/medium", "Python/hard",
    "Java/easy", "Java/medium", "Java/hard"
]

def get_title_from_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("# Title:"):
                    return line.strip()[8:].strip()
                if line.strip().startswith("// Title:"):
                    return line.strip()[9:].strip()
                if line.strip() and not (line.strip().startswith("#") or line.strip().startswith("//")):
                    break
    except Exception:
        return None
    return None

def find_matching_path(logged_path):
    if os.path.exists(logged_path):
        return logged_path
    fname = os.path.basename(logged_path)
    for folder in SOLUTION_FOLDERS:
        candidate = os.path.join(folder, fname)
        if os.path.exists(candidate):
            return candidate
    return None

def read_solved_problems():
    if not os.path.exists(SOLVED_LOG):
        return []
    with open(SOLVED_LOG, "r") as f:
        logged = sorted(set(line.strip() for line in f if line.strip()))
    problems = []
    seen = set()
    for logged_path in logged:
        real_path = find_matching_path(logged_path)
        if real_path and real_path not in seen:
            title = get_title_from_file(real_path)
            problems.append((title or "Unknown Title", real_path))
            seen.add(real_path)
    return problems

def write_problems_list(problems):
    os.makedirs(os.path.dirname(PROBLEMS_LIST_FILE), exist_ok=True)
    with open(PROBLEMS_LIST_FILE, "w", encoding="utf-8") as f:
        f.write("# Solved Problems List\n\n")
        for title, path in problems:
            f.write(f"- {title} ({path})\n")

def update_readme(problems):
    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    if problems:
        new_section = "Solved Problems:\n" + "\n".join(f"- {t} ({p})" for t, p in problems)
    else:
        new_section = "No problems solved yet."
    pattern = re.compile(
        rf"({re.escape(START_MARKER)})(.*)({re.escape(END_MARKER)})",
        re.DOTALL
    )
    updated_content = pattern.sub(f"\\1\n{new_section}\n\\3", content)
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

def main():
    problems = read_solved_problems()
    write_problems_list(problems)
    update_readme(problems)
    print(f"Updated README.md with {len(problems)} problems and titles.")

if __name__ == "__main__":
    main()
