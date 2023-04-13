#!/usr/bin/python3
""" the function for return to json """
import json


def class_to_json(obj):
    """ the function to convert object on json """

    return obj.__dict__
