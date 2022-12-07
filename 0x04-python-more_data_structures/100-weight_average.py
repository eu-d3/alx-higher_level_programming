#!/usr/bin/python3


"""Return the weighted average of integers in a list of tuples."""


def weight_average(my_list=[]):
    if len(my_list) == 0 or not isinstance(my_list, list):
        return 0

    total = 0
    weight = 0
    for tuple_s in my_list:
        total += (tuple_s[0] * tuple_s[1])
        weight += tuple_s[1]
    return (total/weight)
