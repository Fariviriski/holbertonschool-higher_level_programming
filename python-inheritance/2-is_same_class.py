#!/usr/bin/python3
"""
defines class-checking function
"""


def is_same_class(obj, a_class):
    """checks if object is exactly an instance of a given class"""
    if type(obj) == a_class:
        return True
    else:
        return False
