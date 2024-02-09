#!/usr/bin/python3
"""
defines class-check func
"""


def is_same_class(obj, a_class):
    """checks if obj is instance of a given class"""
    if type(obj) == a_class:
        return True
    else:
        return False
