# LeetCode: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
