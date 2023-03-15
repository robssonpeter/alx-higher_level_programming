#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    checker = lambda x: x if x != search else replace

    return list(map(checker, my_list))
