#!/usr/bin/python3

def add_integer(a, b=98):
    allowed_types = [type(1), type(2.1)]
    if type(a) not in allowed_types:
        raise TypeError('a must be an integer')
       
    if type(b) not in allowed_types:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
