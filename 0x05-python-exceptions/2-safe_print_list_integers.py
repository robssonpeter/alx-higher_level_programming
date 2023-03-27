#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    iter = 0
    count = 0
    while (iter < x):
        try:
            print("{:d}".format(my_list[iter]), end="")
            iter = iter + 1
            count = count + 1
        except (TypeError, ValueError):
            print("", end="")
            iter = iter + 1
    print("")
    return count
