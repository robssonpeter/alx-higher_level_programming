#!/usr/bin/python3
""" the function to create a json stting and write to a file """
import json


def save_to_json_file(my_obj, filename):
    """ the function to save to json file """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
