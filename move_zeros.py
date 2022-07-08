# Given an integer array nums, move all 0's to the
# end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def moveZeroes(nums: list) -> None:
    left = 0
    for right in range(len(nums)):
        # Checks if values does not equal zero
        if nums[right]:
            # This just swaps values
            nums[left], nums[right] = nums[right], nums[left]
            # increment pointer
            left += 1
    right += 1
    return nums

moveZeroes([0,1,0,3,12])
