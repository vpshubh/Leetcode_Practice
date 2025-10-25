# Python/easy/two_sum.py
# Title: Two Sum
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    # Example test
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print("Two Sum Result:", result)

    # Log this problem as solved
    with open("solved_problems.txt", "a") as f:
        f.write("Python/easy/two_sum.py\n")

    # Run the README update script
    import subprocess
    subprocess.run(["python", "scripts/update_readme.py"])
