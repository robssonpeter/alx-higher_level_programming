#!/usr/bin/python3
""" instantiate teh student class """
import json


class Student:
    """ the constructor """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ the function that converts the class instanc to json """
        return json.dumps(self.__dict__)

