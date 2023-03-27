#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    returns = 0
    try:
        for num in range(x):
            print(my_list[num], end="")
            returns = returns + 1
    except IndexError:
        print("")
    except TypeError:
        print("Please enter a valid type")
    else:
        print("")
    return returns
