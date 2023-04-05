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

    def area(self):
        """ finds and return the are of the rectancle"""
        return self.__height * self.__width

    def perimeter(self):
        """finds and returns the perimeter of the rectangle """
        if not self.__height or not self.__width:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """ the str function """
        return "\n".join("#"*self.__width for h in range(self.__height))

