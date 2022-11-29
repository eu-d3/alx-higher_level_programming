#!/usr/bin/python3
""""Print the alphabet in reverse order alternating upper- and lower-case."""
for i in range(0, 26, 2):
    print("{:c}{:c}".format(122 - i, (122 - i - 1) - 32), end='')
