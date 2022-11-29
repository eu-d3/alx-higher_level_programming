#!/usr/bin/python3

"""Print numbers from 0 to 98 in A) decimal and B) hexadecimal"""

for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
