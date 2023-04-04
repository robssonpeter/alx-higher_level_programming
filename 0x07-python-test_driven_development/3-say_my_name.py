#!/usr/bin/python3
"""The module say my name"""


def say_my_name(first_name, last_name=""):
    """the function say my name
    """

    if type(first_name) != type('a'):
        raise TypeError('first_name must be a string')

    print(f"My name is {first_name} {last_name}")
