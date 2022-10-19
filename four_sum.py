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

# nums = [-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492]
# target = 1682

# # [1, 0, -2, 2]
# i = 4
# j = 0
# k = 0


def four_sums(nums, target):
    
    result = []
    
    for i in range(len(nums)):

        nums_copy = nums.copy()   
        nums_copy.pop(i)

        
        for j in range(len(nums_copy)):
            
            nums_copy2 = nums_copy.copy()
            nums_copy2.pop(j)
            
            for k in range(len(nums_copy2)):
                nums_copy3 = nums_copy2.copy()
                nums_copy3.pop(k)
            
                target_residual = target - (nums[i] + nums_copy[j] + nums_copy2[k])
                if target_residual in nums_copy3: 

                    solution = [nums[i], nums_copy[j], nums_copy2[k], target_residual]
                    solution.sort()
                    
                    result.append(solution)
                else: continue
       
    result.sort()
    result = list(result for result, _ in itertools.groupby(result))
    
    return result
    
start_time = time.time()    
res = four_sums(nums, target)  
print(res)
print("--- %s seconds ---" % (time.time() - start_time))





    