#!/usr/bin/python3


class MyList(list):
    """ My List Class """

    def print_sorted(self):
        """ The function that prints the sorted list of items """

        self.sort()
        print(self)
