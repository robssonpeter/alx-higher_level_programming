#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle
""" Defines the class Square inheriting rectangle """


class Square(Rectangle):
    """ the constructor function """

    def __init__(self, size):
        """ Construct initializing variables """

 
        self.integer_validator("size", size)
        self.__size = size

    def area():
        """ finds the square as the area of square """

        return self.__size**2
