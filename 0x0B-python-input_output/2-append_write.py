#!/usr/bin/python3

""" The function that opens and append text in a file """


def append_write(filename="", text=""):
    """ opens a file for appending purposes """

    with open(filename, "a", encoding="utf-8") as f:
        """ append some texts to file """

        return f.write(text)
