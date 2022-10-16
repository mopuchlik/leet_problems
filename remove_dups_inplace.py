# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:17:45 2022

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears 
only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, 
you must instead have the result be placed in the first part of the array 
nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this 
by modifying the input array in-place with O(1) extra memory.

@author: User
"""

nums = [0,0,1,1,1,2,2,3,3,4]

def remove_dups(nums):
    
    n_els = len(nums)
    
    val_init = nums[0]
    val_new = val_init
    
    shift = 0
    n_unique = 1

    for i in range(1, n_els):

        if val_new != nums[i]:
            val_new = nums[i]
            n_unique += 1
            if shift == 0:
                continue
            else:
              nums[i - shift] = nums[i]  
        else:
            shift += 1
            
    return n_unique            
    
print(remove_dups(nums))
print(nums)


