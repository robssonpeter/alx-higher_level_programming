#!/usr/bin/python3

""" The function to write into a file """


def write_file(filename="", text=""):
    """ opens a filename and puts some text to it """

    with open(filename, "w", encoding="utf-8") as f:
        """ get the file """

        return f.write(text)
