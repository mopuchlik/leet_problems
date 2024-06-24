# %%
"""
Created on Fri Oct 14 14:55:28 2022

Given a sorted array of distinct integers and a target value, return 
the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

@author: User
"""


nums = [1, 3, 5]
target = 4

# import math

# %%


def ret_index(nums, target):

    pos_start = 0
    pos_end = len(nums) - 1

    if nums[pos_start] >= target:
        return pos_start
    if nums[pos_end] < target:
        return pos_end
    if nums[pos_end] == target:
        return pos_end + 1

    while pos_start != pos_end:

        pos_mid = pos_start + (pos_end - pos_start) // 2

        if nums[pos_mid] < target:
            if pos_start == pos_mid:
                return pos_start + 1

            pos_start = pos_mid

        elif nums[pos_mid] > target:

            pos_end = pos_mid
        else:
            break

    return pos_mid


# %%

pos = ret_index(nums, target)
# %%
