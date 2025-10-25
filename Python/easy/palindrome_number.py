# Title: Palindrome Number

def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindrome
    if x < 0:
        return False
    # Convert to string and compare with reverse
    s = str(x)
    return s == s[::-1]

if __name__ == "__main__":
    x = 121
    result = is_palindrome(x)
    print(f"Is {x} palindrome?:", result)

    # Log this problem as solved
    with open("solved_problems.txt", "a") as f:
        f.write("Python/easy/palindrome_number.py\n")

    # Run the README update script
    import subprocess
    subprocess.run(["python", "scripts/update_readme.py"])
