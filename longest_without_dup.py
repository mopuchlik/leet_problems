#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:05:06 2023

https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest
substring
without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



@author: michal
"""


# %%
def lengthOfLongestSubstring(s: str) -> int:

    max_count = 0

    for i in range(len(s)):

        s_temp = s[i]
        j = 1   

        while i + j < len(s) and s[i + j] not in s_temp:
            s_temp += s[i + j]
            j += 1
        if max_count < j:
            max_count = j
            sol = s_temp
    return max_count


# %%
s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"

# s = "au"
# s = " "


print(lengthOfLongestSubstring(s))
