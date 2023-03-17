# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:40:02 2023
The first line of input contains the original string. The next line contains the substring.

Each character in the string is an ascii character. 

Output the integer number indicating the total number of occurrences of the substring in the original string. 

ABCDCDC
CDC

output = 2



@author: User
"""



string = "ininini"
sub_string = "ini"

string = "ABCDCDC"
sub_string = "CDC"


def count_substring(string, sub_string):
    
    count = 0
    
    n_string = len(string)
      
    while n_string > 0:
        ind = string.find(sub_string)
        if ind == -1: 
            break
        count += 1
        n_string = n_string - ind -1
        string  = string[(ind + 1):]
    
    return count


count_substring(string, sub_string)
