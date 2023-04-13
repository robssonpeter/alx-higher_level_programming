#!/usr/bin/python3
""" the function to create an object from json """
import json


def load_from_json_file(filename):
    """ the function it self """

    with open(filename) as f:
        return json.loads(f.read())
