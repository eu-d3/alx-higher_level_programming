#!/usr/bin/python3


"""Multiplies all values of a dictionary by 2"""


def multiply_by_2(a_dictionary):
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
