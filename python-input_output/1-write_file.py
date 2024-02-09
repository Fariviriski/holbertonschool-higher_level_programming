#!/usr/bin/python3
"""defines function write_file"""


def write_file(filename="", text=""):
    """returns num of chars written to file"""
    with open(filename, "W", encoding="utf-8") as f:
        return f.write(text)
