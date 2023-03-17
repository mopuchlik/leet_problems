# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:06:21 2023

@author: michal
"""

# s = set("Hacker")
# print(s.intersection("Rank"))


group1 = "1 2 3 4 5 6 7 8 9"
group1 = group1.split(" ")

group2 = "10 1 2 3 11 21 55 6 8"
group2 = group2.split(" ")


group1_s = set(group1)
group2_s = set(group2)

print(len(group1_s.intersection(group2_s)))




