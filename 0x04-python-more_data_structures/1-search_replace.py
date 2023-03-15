#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    def checker(number):
        return number if number != search else replace

    return list(map(checker, my_list))
