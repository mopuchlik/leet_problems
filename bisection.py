# -*- coding: utf-8 -*-
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


nums = [1,3, 5]  
target = 4

import math


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
        
def ret_index(nums, target):    
    
    ind_start = 0
    ind_end = len(nums) - 1
            
    if nums[ind_start] >= target: 
        return ind_start
    
    elif nums[ind_end] < target:
        return ind_end + 1
      
    elif nums[ind_end] == target:
        return ind_end
    
    while ind_end != ind_start:
        
        ind_bisect = ind_start + math.floor((ind_end - ind_start) / 2)
        
        if nums[ind_bisect] < target:
            if ind_start == ind_bisect:
                return ind_start + 1
            else:
                ind_start = ind_bisect
                ind_bisect = ind_start + math.floor((ind_end - ind_start) / 2) 

        
        elif nums[ind_bisect] > target:
            ind_end = ind_bisect
            ind_bisect = ind_start + math.floor((ind_end - ind_start) / 2)
            
        else: break  

    return ind_bisect


print(ret_index(nums, target))
