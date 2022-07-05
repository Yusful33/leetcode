# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there
# to ensure the merge result can fit in nums1.

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?


def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    if m == 0:
        nums1 = nums2
        return nums1
    elif n == 0:
        return nums1
    else:
        nums1 = list(set(sorted(nums1 + nums2)))
        return nums1


test1 = merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)


def ideal_merge(nums1: list, m: int, nums2: list, n: int) -> None:
    print(nums1, nums2)
    left, right = 0, 0
    # n = 3 and m = 3
    for right in range(n):
        # 0 < (3+0) and nums2[0] > nums1[0]
        # Doing this while loop until left = 3
        print(f"Left {left}, right {right} and nums1 {nums1}")
        while (left < m + right) and nums2[right] > nums1[left]:
            left += 1
            print(nums1)
        # inserts num2 at left index which is a min of 3
        nums1.insert(left, nums2[right])
    # Sets nums1 equal to the end of nums2
    # nums[3+2+1] = nums1[6] = 0
    # nums2[2+1:] = nums2[3] = does not exist
    # removes trailing zeros from num1 list
    nums1[m + right + 1 :] = nums2[right + 1 :]
    print(nums1)


ideal_merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
