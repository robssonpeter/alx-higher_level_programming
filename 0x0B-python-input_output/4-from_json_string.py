#!/usr/bin/python3
""" the function to convert json string to object """
import json


def from_json_string(my_str):
    """ converts strig to object """

    return json.loads(my_str)
