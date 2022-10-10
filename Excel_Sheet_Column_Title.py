# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:12:21 2022

@author: User
"""


# Given an integer columncolumnNumber, return its corresponding column title as it appears in an Excel sheet.

#%%
columnNumber = 701
# must be 'ZY'

result = []
# n = 1 
while columnNumber  != 0:
    
    result_tmp = columnNumber % (26)
    if result_tmp == 0: 
        result_tmp = 26
    result.append(result_tmp)

    columnNumber = int((columnNumber - result_tmp ) / 26)
    
result = result[::-1]

result_chr = ''
for i in range(len(result)):
    result_chr += chr(ord('@') + result[i])

print(result_chr)
