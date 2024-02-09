#!/usr/bin/python3
"""defines a text-file reading function"""


def read_file(filename=""):
    """prints utf-8 content to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
