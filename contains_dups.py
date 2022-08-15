## Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Example 
# Input: nums = [1,2,3,1]
# Output: true


def contain_dups(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True

value = contain_dups([1,2,3,1])
print(value)