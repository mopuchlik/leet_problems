# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:09:25 2022

create cartesia superposition of dictionaries without using 
itertools.product() function

@author: User
"""

# import ipdb


input = {
"szerokosc": {"20cm", "16cm", "10cm"},
"wysokosc": {"30cm", "40cm"},
"kolor": {"czarny", "biały", "zielony"}
}


def prod_final(input): 

    def product(ar_list):
        if not ar_list:
            yield ()
        else:
            for a in ar_list[0]:
                for prod in product(ar_list[1:]):
                    yield (a,) + prod
                    
                    
    keys = list(input.keys())
    values = list(input.values())
    values_cart = list(product(values))
    
    result = []
    for i in range(len(values_cart)):
        dict_row = dict(zip(keys, values_cart[i]))
        result.append(dict_row)
    
    return(result)

print(prod_final(input))


# # other solution
# input = {
# "szerokosc": {"20cm", "16cm", "10cm"},
# "wysokosc": {"30cm", "40cm"},
# "kolor": {"czarny", "biały", "zielony"}
# }

# def product1(*args, **kwds):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = map(tuple, args) * kwds.get('repeat', 1)
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     for prod in result:
#         yield tuple(prod)


# keys = list(input.keys())
# values = list(input.values())
# values_cart = list(product1(values))

# result = []
# for i in range(len(values_cart)):
#     dict_row = dict(zip(keys, values_cart[i]))
#     result.append(dict_row)

# print(result)