#!/usr/bin/python3
"""
defines class-checking function
"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a given class.
    args:
    obj (any): object to be checked.
    a_class(type): class to match the object to
    Returns: True if is instance, False otherwise
    """
    if type(obj) == a_class:
        return True
    return False
