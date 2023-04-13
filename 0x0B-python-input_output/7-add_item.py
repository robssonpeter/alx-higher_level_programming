#!/usr/bin/python3
""" Defines the function to read agruments and add to list """


from sys import argv
import json

""" import save data to a file """
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    prev = load_from_json_file("add_item.json")
    if len(prev) == 0:
        prev = []
    args = argv[1:]

    new = prev + args

    save_to_json_file(new, "add_item.json")
