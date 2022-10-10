#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 23:29:31 2022

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

@author: michal
"""

strs = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]


def com_pref(strs):
    common_pref = strs[0]

    for i in range(1, len(strs)):
        str_temp = strs[i]
        j = 0
        while (
            j <= len(common_pref) - 1
            and j <= len(str_temp) - 1
            and str_temp[j] == common_pref[j]
        ):
            j += 1
        common_pref = common_pref[0:j]
    return common_pref


x = com_pref(strs)
print(x)

y = com_pref(strs2)
print(y)
