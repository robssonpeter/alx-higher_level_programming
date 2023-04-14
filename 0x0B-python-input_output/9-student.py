#!/usr/bin/python3
""" instantiate teh student class """


class Student:
    """ the constructor """

    def __init__(self, first_name, last_name, age):
        """ initializting the variables

        Args:
            first_name (str): the first name
            last_name (str): the last name
            age (int): the age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ the function that converts the class instanc to json """

        class_to_json = __import__("8-class_to_json").class_to_json
        return class_to_json(self)
