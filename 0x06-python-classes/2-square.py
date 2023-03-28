#!/usr/bin/python3
"""The class instance"""


class Square:
    """ the constructor """
    def __init__(self, size=0):
        if type(1) == type(size):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
