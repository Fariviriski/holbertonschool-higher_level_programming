#!/usr/bin/python3
"""defines a Python class to json function"""


def class_to_json(obj):
    """returns the dictionary representation of a simple data structure"""
    return obj.__dict__
