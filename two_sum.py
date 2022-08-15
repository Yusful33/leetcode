# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# def twoSum(nums, target):
#     return_list = list()
#     right = len(nums) - 1
#     while right > 0:
#         for left in range(len(nums)):
#             if (nums[left] + nums[right]) == target:
#                 return_list.append(left)
#                 return_list.append(right)
#             else:
#                 right -= 1 
#             print(left, right)
#         return return_list

def twoSum(nums, target):
    # Testing with [2,7,11,15], 9
    prevMap = dict()
    # i = 0 and n = 2
    for i, n in enumerate(nums):
        # diff = 7
        diff = target - n 
        if diff in prevMap:
            print([prevMap[diff], i])
        # prevMap is blank is first value is 2: 0 
        prevMap[n] = i
check = twoSum([2,7,11,15], 9)
# print(check)