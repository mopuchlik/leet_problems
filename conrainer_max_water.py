# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:14:16 2023

https://leetcode.com/problems/container-with-most-water/
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented 
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
(blue section) the container can contain is 49.


@author: michal
"""

#%% 
import time

#%% version with optimization wrt max height for j (ugly)
# def maxArea(height):
#     vol = 0
    
#     for i in range(len(height)):
#         height_j_max = height[-1]
#         for j in range(len(height)):
            
#             if i < len(height) - j - 1:
#                 if height[len(height) - j - 1] >= height_j_max:
#                     vol_temp = min(height[i], height[len(height) - j - 1]) * (len(height) - j - 1 - i)
#                     if height_j_max != height[len(height) - j - 1]:
#                         height_j_max = height[len(height) - j - 1]
#                     if vol_temp > vol:
#                         vol = vol_temp
#                 else: continue        
#             else: break
#     return vol    
        
#%% version with optimization wrt max height for j (nicer)    

# def maxArea(height):
#     vol = 0

#     for i in range(len(height)):
#         height_j_max = height[-1]
#         for j in range(len(height)):
            
#             if i < len(height) - j - 1:
#                 # calculate only if h[j-1] >= h_j_max 
#                 if height[-j - 1] >= height_j_max:
#                     vol_temp = min(height[i], height[-j - 1]) * (len(height) - j - 1 - i)
#                     if height_j_max != height[-j - 1]:
#                         height_j_max = height[-j - 1]
#                     if vol_temp > vol:
#                         vol = vol_temp
#                 else: continue        
#             else: break
#     return vol

#%% version with optimization wrt max height for j and i   
# def maxArea(height):
#     vol = 0

#     height_i_max = height[0]
#     for i in range(len(height)):
#         # calculate only if h[i] >= h_i_max 
#         if i == 0 or height[i] > height_i_max:
#             height_i_max = height[i]
            
#             height_j_max = height[-1]
#             for j in range(len(height)):
                
#                 if i < len(height) - j - 1:
#                     # calculate only if h[j-1] >= h_j_max 
#                     if j == 0 or height[-j - 1] > height_j_max:
#                         height_j_max = height[-j - 1]
                        
#                         vol_temp = min(height[i], height[-j - 1]) * (len(height) - j - 1 - i)
#                         if vol_temp > vol:
#                             vol = vol_temp
#                     else: continue        
#                 else: break
#             else: continue   
#     return vol

#%% quickest -- compares left and right border
def maxArea(height):
    
    i = 0
    j = len(height) - 1

    vol = min(height[i], height[j]) * (j - i)

    while i != j:
        if height[i] < height[j]:
            
            i += 1 
            if height[i] > height[i-1] and i != j:
               vol = max(vol , min(height[i], height[j]) * (j-i))
        else: 
            j -= 1
            if height[j] > height[j + 1] and i != j:
                vol = max(vol , min(height[i], height[j]) * (j-i))

    return vol





height = [1,8,6,2,5,4,8,3,7]
# height = [1, 1]
# height = [1, 1, 1]

# height = [2,3,10,5,7,8,9]
# 10 8
# 3, 1

maxArea(height)

#%%

start_time = time.time()    
res = maxArea(height)  
print(res)
print("--- %s seconds ---" % (time.time() - start_time))


    
    
    
    

