#!/usr/bin/python3
"""
prints the ASCII alphabet, in lowercase, not followed by a new line.
Print all the letters except q and e
"""
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
