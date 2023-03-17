# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:44:20 2023

Let's learn about list comprehensions! You are given three integers and representing the dimensions of a cuboid along 
with an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of is *not* equal to n. 


Example
x = 1
y = 1
z = 2
n = 3    


output 
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

@author: User
"""

x = 1
y = 1
z = 2
n = 3  

# result = []

# for x in range(x+1):
#     for y in range(y+1):
#         for z in range(z+1):
#             if x + y + z != n:
#                 result.append([x, y, z])



x = 1
y = 1
z = 1
n = 2  
res = [[a, b, c] for a in range(x + 1) for b in range(y+1) for c in range(z+1) if a + b + c <= n]








def fizzBuzz(n):
    # Write your code here
    
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")  
    elif n % 3:
        print("Fizz")
    elif n % 5:  