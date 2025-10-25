# Title: Valid Parentheses

def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False
    return not stack

if __name__ == "__main__":
    test_str = "()[]{}"
    print(f"Is '{test_str}' valid?:", is_valid(test_str))

    with open("solved_problems.txt", "a") as f:
        f.write("Python/medium/valid_parentheses.py\n")

    import subprocess
    subprocess.run(["python", "scripts/update_readme.py"])
