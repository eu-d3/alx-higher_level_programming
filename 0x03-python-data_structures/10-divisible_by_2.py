#!/usr/bin/python3


""" Finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    
    if len(my_list) == 0:
                return None
    
    multiples = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    
    return (multiples)
