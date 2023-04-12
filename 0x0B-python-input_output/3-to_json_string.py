#!/usr/bin/python3
import json
from io import StringIO

""" The function for encoding to json """


def to_json_string(my_obj):
    """ encode the string """

    io = StringIO()

    json.dump(my_obj, io)

    return io.getvalue()
