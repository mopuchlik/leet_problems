# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2 
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Created on Sun Mar  5 00:30:46 2023

@author: User
"""
#%%

import time

#%% first version  
# def threeSum(nums):
    
#     result = []
    
#     for i in range(len(nums) - 2):
#         for j in range(i + 1, len(nums) - 1):
#                 target = -(nums[i] + nums[j])
#                 if target in nums[(j+1):]: 

#                     solution = [nums[i], nums[j], target]
#                     solution.sort()
                    
#                     if solution not in result:
#                         result.append(solution)
#                 else: continue

#     return result

#%% with sorting test111

def threeSum(nums):
    
    result = []
    
    # sort first
    nums.sort()
    
    for x in range(len(nums)-2):
       
        i = x + 1
        j = len(nums) - 1
       
        while i < j:
            s1 = nums[i] + nums[x] + nums[j]
        
            if s1 == 0: 
                sol = [nums[i], nums[x], nums[j]]
                sol.sort()
                
                if sol not in result:
                    result.append(sol)
        
            if s1 < 0:
                i += 1
            else:  
                j -= 1
    return result        


#%%
nums = [-1,0,1,2,-1,-4]

nums = [0,1,1]

nums = [0,0,0]

#%%

start_time = time.time()    
res = threeSum(nums)  
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
