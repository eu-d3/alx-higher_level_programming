#!/usr/bin/python3


"""The largest integer from a list"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    largest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]

    return (largest)
