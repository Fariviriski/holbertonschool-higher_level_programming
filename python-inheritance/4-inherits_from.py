#!/usr/bin/python3
"""defines an inherited class-check function"""


def inherits_from(obj, a_class):
    """checks if object is inherited instance of class
    Args:
        obj (any): the object to checks
        a_class (type): the class to match object to
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
