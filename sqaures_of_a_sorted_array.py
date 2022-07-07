# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def sortedSquares(nums: list) -> list:
    n_nums = list()
    left, right = 0, len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            print(f'left: {nums[left]} and right: {nums[right]}')
            n_nums.append(nums[left] ** 2)
            left += 1
        else:
            print(f'left: {nums[left]} and right: {nums[right]}')
            n_nums.append(nums[right] ** 2)
            right -= 1
    print(n_nums)
    return n_nums[::-1]


result = sortedSquares([-5,-3,-2,-1])
print(result)
