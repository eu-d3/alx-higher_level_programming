#!/usr/bin/python3

"""Check for lowercase characters."""


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
