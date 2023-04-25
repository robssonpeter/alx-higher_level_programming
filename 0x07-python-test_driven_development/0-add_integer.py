#!/usr/bin/python3
"""module for add ing iteger
"""


def add_integer(a, b=98):
    """function add_integer"""
    allowed_types = [type(1), type(2.1)]
    if type(a) not in allowed_types:
        raise TypeError('a must be an integer')
       
    if type(b) not in allowed_types:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
