#!/usr/bin/python3


"""Replaces an element in a list at a specific position,
without modifying the original"""


def new_in_list(my_list, idx, element):
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list[:]
    new_list[idx] = element
    return (new_list)
