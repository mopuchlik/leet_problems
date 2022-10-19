# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 23:58:27 2022

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

@author: User
"""

import itertools
import time

nums = [1,0,-1,0,-2,2]
target = 0

# nums = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
# target = 200

# # [1, 0, -2, 2]
# i = 4
# j = 0
# k = 0


def four_sums(nums, target):
    
    result = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                target_residual = target - (nums[i] + nums[j] + nums[k])
                if target_residual in nums[(k+1):]: 

                    solution = [nums[i], nums[j], nums[k], target_residual]
                    solution.sort()
                    
                    if solution not in result:
                        result.append(solution)
                else: continue 
       
    # result.sort()
    # result_unique = list(result for result, _ in itertools.groupby(result))
    
    # result_unique = []
    # for i in range(len(result)):
    #     if result[i] not in result_unique:
    #         result_unique.append(result[i])

    return result


start_time = time.time()    
res = four_sums(nums, target)  
print(res)
print("--- %s seconds ---" % (time.time() - start_time))




    