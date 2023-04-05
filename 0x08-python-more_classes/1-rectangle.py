#!/usr/bin/python3
"""The rectangle class"""


class Rectangle:
    """inside the rectangel class"""

    def __init__(self, width=0, height=0):
        """the constructor"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if not isinstance(value, type(1)):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise TypeError('width must be an integer')
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, type(1)):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be an integer')
        self.__height = value
