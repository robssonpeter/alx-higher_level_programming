#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())

    if value not in values:
        return a_dictionary

    index = values.index(value)
    key = keys[index]

    del a_dictionary[key]
    del values[index]
    if value in values:
        return complex_delete(a_dictionary, value)
    return a_dictionary
