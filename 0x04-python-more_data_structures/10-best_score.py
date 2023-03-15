#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    max_value = 0

    for val in values:
        if val > max_value:
            max_value = val

    index = values.index(max_value)
    return keys[index]
