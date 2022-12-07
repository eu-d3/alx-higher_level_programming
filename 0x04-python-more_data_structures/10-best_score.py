#!/usr/bin/python3


"""Returns the key with the biggest integer value."""


def best_score(a_dictionary):
    high_count = 0
    maximum = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > high_count:
                high_count = value
                highest_score = key
    return highest_score
