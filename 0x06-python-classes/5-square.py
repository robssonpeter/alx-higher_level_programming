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

    """ the area method """
    def area(self):
        return self.__size**2

    @property
    def size(self):
        """getter of __size
        Returns:
            Size of square
        """
        return self.__size

    """ the size setter """
    @size.setter
    def size(self, value):
        if type(1) == type(value):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
