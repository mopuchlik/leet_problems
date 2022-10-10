#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 12:52:03 2022

@author: michal
"""

#%%
a = [2, 4, 7, 2, 2]
b = [3]

x = a + b

y = x.sort()

y = sorted(x)

x is y

v = enumerate(x)


#%%


x

type(x)


a = (
    2,
    2,
)
b = (3,)

type(a)


a + b


y = {1: 'b', 
     2: 'c'}

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   else: print('Current Letter : h')
   
   print('Current Letter :' + letter)
   


