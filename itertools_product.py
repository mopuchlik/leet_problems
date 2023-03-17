# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 17:29:38 2023

@author: User
"""
from itertools import product

# X = input()
# Y = input()

# X = "1 2"
# Y = "2 3"

X = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19"
Y = "0 1"

x_list_str = X.split(" ")
x_list_int = [int(x) for x in x_list_str]
y_list_str = Y.split(" ")
y_list_int = [int(y) for y in y_list_str]


#print(X[0])
#A = [int(character) for character in X if character != " "]
#B = [int(character) for character in Y if character != " "]


# prod = list(product(A, B))
prod = product(x_list_int, y_list_int)
print(*prod)

# print(*range(1, 6))


