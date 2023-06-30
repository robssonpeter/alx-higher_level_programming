#!/usr/bin/python3
""" The function to find the peak of a list """

def find_peak(list_of_integers):
    """ The body of the function"""

    peak = None
    if len(list_of_integers) > 2:
        rnge = range(1, len(list_of_integers))
        for n in rnge:
            left = list_of_integers[n - 1]
            right = list_of_integers[n + 1]
            curr = list_of_integers[n]
            if curr >= left and curr >= right:
                return curr
    return peak
