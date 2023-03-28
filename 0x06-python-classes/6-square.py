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

    @property
    def position(self):
        """ getter of property
        Returns:
            the poistion
        """
        return self.position

    @position.setter
    def position(self, value):
        if type((1, 1)) == type(value) and len(value) == 2:
            if value[0] >= 0 and value[1] >= 0:
                self.position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ my print function """
    def my_print(self):
        for y in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
