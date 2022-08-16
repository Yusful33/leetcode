# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
from collections import Counter 
def singleNumber(nums):
    # Handling the base case
    if len(nums) < 2:
        return nums[0]
    tracker = Counter(nums)
    print(tracker)
    for key, value in tracker.items():
        if value == 1:
            return key


test = singleNumber([1, 2, 2, 6, 9, 14, 13, 6, 9, 1, 13])
print(test)