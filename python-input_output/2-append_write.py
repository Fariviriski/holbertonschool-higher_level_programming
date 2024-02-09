#!/usr/bin/python3
"""defines a file-appending func"""

def append_write(filename="", text=""):
   """appends a string to enf of utf-8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
