import subprocess

def log_and_update(solution_path):
    print(f"Logging {solution_path} and updating README...")  # Debug print, optional
    with open("solved_problems.txt", "a") as f:
        f.write(f"{solution_path}\n")
    subprocess.run(["python", "scripts/update_readme.py"])
    print("README updated.")  # Debug print, optional
