# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:53:17 2022

@author: User
"""

# ### take a list and find indices that sum to target
# ### assumptions: solution exist and indices must differ


# import ipdb
# ipdb.set_trace()

nums = [3,2,4]
target = 6

n = len(nums)

for i in range(n):
    for k in range(i + 1, n):
        if nums[i] + nums[k] == target:
            result = [i, k]
            break

