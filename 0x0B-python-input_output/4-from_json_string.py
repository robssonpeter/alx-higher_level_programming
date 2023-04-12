#!/usr/bin/python3
import json

""" the function to convert json string to object """


def from_json_string(my_str):
    """ converts strig to object """

    return json.loads(my_str)
