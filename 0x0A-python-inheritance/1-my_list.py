#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """ implementation of sorted list of items """

    def print_sorted(self):
        """ The function that prints the sorted list of items """

        """ prints the sorted list."""
        print(sorted(self))
