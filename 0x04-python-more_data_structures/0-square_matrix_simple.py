#!/usr/bin/python3


"""Compute the square value of integers in a matrix"""


def square_matrix_simple(matrix=[]):
    return ([list(map(lambda x: x * x, row)) for row in matrix])
