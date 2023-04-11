#!/usr/bin/python3

def inherits_from(obj, a_class):
    """ checks if object inherits a class """
    
    is_self = type(obj) == a_class
    return issubclass(type(obj), a_class) and not is_self
