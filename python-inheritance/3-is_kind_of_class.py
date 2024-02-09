#!/usr/bin/python3
"""defines a class and inherited class-check function"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance or inherited instance of class
    Args:
        obj (any): the object to checks
        a_class (type): class to match the type to
    Returns:
        True if obj is an instance pr inherited instance of a_class
        False otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
