# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:10:04 2022

@author: User
"""

# ### Given an integer x, return true if x is palindrome integer.
# ### An integer is a palindrome when it reads the same backward as forward.

def isPalindrome(x):
    x = str(x)
    for i in range(int(len(x) / 2)):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True




