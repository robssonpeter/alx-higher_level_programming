#!/usr/bin/python3
for x in range(122, 96, -1):
    if (x % 2 == 0):
        print("{char}".format(char=chr(x)), end="")
    else:
        print("{char}".format(char=chr(x-32)), end="")
