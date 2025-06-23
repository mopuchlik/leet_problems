# Given an integer array nums, find the subarray (continuous index preserved)
# with the largest sum,
# and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

import numpy as np


def maxSubArray(nums):

    if len(nums) == 1:
        return nums[0]
    res = -np.inf
    for i in range(len(nums)):
        cum_sub = [sum(nums[i:k]) for k in range(i + 1, len(nums) + 1)]
        if max(cum_sub) >= res:
            res = max(cum_sub)

    return res


# nums = [5, 4, -1, 7, 8]
# nums = [1]
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res = maxSubArray(nums)
print(res)
