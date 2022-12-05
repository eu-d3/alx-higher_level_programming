#!/usr/bin/python3


"""Removes all appearances of 'c' & 'C' from a string"""


def no_c(my_string):
    str_minus_C = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            str_minus_C += my_string[i]
    return (str_minus_C)
