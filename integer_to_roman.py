# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:20:46 2023

https://leetcode.com/problems/integer-to-roman/

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900

1 <= num <= 3999

Input: num = 3
Output: "III"

Input: num = 58
Output: "LVIII"

Input: num = 1994
Output: "MCMXCIV"

@author: User
"""

#%%
def intToRoman(num: int) -> str:
    
    num = str(num)
    
    i = len(num) - 1
    counter = 1
    
    while i >= 0:
         
        num_temp = num[i]
        
        if counter == 1:
            if num_temp == "0":
                sol_temp = ""
            elif num_temp == "1": 
                sol_temp = "I"
            elif num_temp == "2": 
                sol_temp = "II"    
            elif num_temp == "3": 
                sol_temp = "III" 
            elif num_temp == "4": 
                sol_temp = "IV" 
            elif num_temp == "5": 
                sol_temp = "V" 
            elif num_temp == "6": 
                sol_temp = "VI"
            elif num_temp == "7": 
                sol_temp = "VII"
            elif num_temp == "8": 
                sol_temp = "VIII"     
            elif num_temp == "9": 
                sol_temp = "IX"
                
            sol = sol_temp    
                
        elif counter == 2:
            if num_temp == "0":
                sol_temp = ""
            elif num_temp == "1": 
                sol_temp = "X"
            elif num_temp == "2": 
                sol_temp = "XX"    
            elif num_temp == "3": 
                sol_temp = "XXX" 
            elif num_temp == "4": 
                sol_temp = "XL" 
            elif num_temp == "5": 
                sol_temp = "L" 
            elif num_temp == "6": 
                sol_temp = "LX"
            elif num_temp == "7": 
                sol_temp = "LXX"
            elif num_temp == "8": 
                sol_temp = "LXXX"     
            elif num_temp == "9": 
                sol_temp = "XC"
            sol = sol_temp + sol       
    
        elif counter == 3:
            if num_temp == "0":
                sol_temp = ""
            elif num_temp == "1": 
                sol_temp = "C"
            elif num_temp == "2": 
                sol_temp = "CC"    
            elif num_temp == "3": 
                sol_temp = "CCC" 
            elif num_temp == "4": 
                sol_temp = "CD" 
            elif num_temp == "5": 
                sol_temp = "D" 
            elif num_temp == "6": 
                sol_temp = "DC"
            elif num_temp == "7": 
                sol_temp = "DCC"
            elif num_temp == "8": 
                sol_temp = "DCCC"     
            elif num_temp == "9": 
                sol_temp = "CM"
            
            sol = sol_temp + sol              
        
        elif counter == 4:
            if num_temp == "1": 
                sol_temp = "M"
            elif num_temp == "2": 
                sol_temp = "MM"    
            elif num_temp == "3": 
                sol_temp = "MMM" 
            sol = sol_temp + sol                 
               
        num = num[:-1] 
        i -= 1
        counter += 1
    
    return sol

#%%

num = 3
# num = 58
# num = 1994

intToRoman(num)
