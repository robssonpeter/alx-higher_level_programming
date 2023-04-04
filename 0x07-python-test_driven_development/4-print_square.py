#!/usr/bin/python3
"""Module for printing a square
"""

def print_square(size):
    """Function for printing square
    """

    if not isinstance(size, type(1)):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError('size must be >= 0')

    for row in range(size):
        for hs in range(size):
            print("#", end="")
        print("")
