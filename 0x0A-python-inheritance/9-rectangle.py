#!/usr/bin/python3
""" Define the class BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ the class rectangle """

    def __init__(self, width, height):
        """ the constructor """

        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ the function that computes the are of rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ the str function that the name of the class """

        return f"[Rectangle] {self.__width}/{self.__height}"
