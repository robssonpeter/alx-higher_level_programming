#!/usr/bin/python3

class BaseGeometry:
    """ The base geometry class is empty """

    def area(self):
        """ The function area to raise exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates a value if it is integer """

        if not isinstance(value, int) and type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0 and type(value) is int:
            raise ValueError(f"{name} must be greater than 0")
