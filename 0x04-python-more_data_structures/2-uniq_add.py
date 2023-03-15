#!/usr/bin/python3

def uniq_add(my_list=[]):
    cleaned = list(set(my_list))

    sum = 0
    for x in cleaned:
        sum = sum + x
    return sum
