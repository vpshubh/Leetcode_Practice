import os
import subprocess
from datetime import datetime

def run_cmd(cmd):
    """Run shell command and return output."""
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"⚠️ Error: {result.stderr.strip()}")
    return result.stdout.strip()

def main():
    print("🔍 Checking git status...")
    status_output = run_cmd("git status --porcelain")

    if not status_output:
        print("✅ No changes detected. Everything is up to date!")
        return

    print("🧠 Detected changes:")
    print(status_output)

    # Auto-commit message with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Auto-update: LeetCode solutions ({timestamp})"

    # Stage all changes
    run_cmd("git add .")

    # Commit changes
    run_cmd(f'git commit -m "{commit_msg}"')

    # Detect current branch
    branch = run_cmd("git branch --show-current")

    # Push changes
    run_cmd(f"git push origin {branch}")

    print(f"🚀 All changes pushed successfully to branch '{branch}' at {timestamp}!")

if __name__ == "__main__":
    main()

    from scripts.utils import log_and_update
    log_and_update("scripts/auto_commit_push.py")   
# --- IGNORE ---

