#!/usr/bin/python3

""" the function to read a text file in utf8 """


def read_file(filename=""):
    """ opens the file specified in filename variable """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
