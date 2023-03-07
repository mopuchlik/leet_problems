# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:06:21 2023

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.


Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


@author: michal
"""

#%%
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        ind = haystack.find(needle)
        
        return ind
        
#%%        
haystack = "baaabbb"
needle = "aaa"

haystack = "sadbutsad"
needle = "sad"
#%%
        
print(strStr(haystack, needle))











        
        


