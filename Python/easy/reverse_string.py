# Title: Reverse String

from typing import List

def reverse_string(s: List[str]) -> None:
    """Reverse string in-place"""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

if __name__ == "__main__":
    s = list("hello")
    reverse_string(s)
    print("Reversed String:", ''.join(s))

    # Log this problem as solved
    with open("solved_problems.txt", "a") as f:
        f.write("Python/easy/reverse_string.py\n")

    # Run the README update script
    import subprocess
    subprocess.run(["python", "scripts/update_readme.py"])
