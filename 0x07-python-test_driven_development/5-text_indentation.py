#!/usr/bin/python3
"""Module for text indentation
"""


def text_indentation(text):
    """Function for printing text indentaiton
    """

    if not isinstance(text, type(text)):
        raise TypeError('text must be a string')
    length = len(text)
    characters = ['.', '?', ':']
    x = 0
    for index in range(length):
        if text[index] in characters:
            print(text[index])
            print("")
            x = 0
        else:
            if x == 0 and text[index] == " ":
                continue
            print(text[index], end="")
            x = 1
