#!/usr/bin/python3

import hidden_4 as hid


"""Print all names defined by hidden_4 module (hid)"""


if __name__ == "__main__":
    names = dir(hid)
    for name in names:
        if name[:2] != "__":
            print(name)
