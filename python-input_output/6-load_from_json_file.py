#!/usr/bin/python3
"""defines a json file-reading function"""
import json


def load_from_json_file(filename):
    """create a Python object from a json file"""
    with open(filename) as f:
        return json.load(f)
