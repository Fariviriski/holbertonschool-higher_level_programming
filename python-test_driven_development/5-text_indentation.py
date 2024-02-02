#!/usr/bin/python3
"""
module that defines text_indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after : . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in [".", "?", ":"]:
        if c in text:
            text = text.replace(c, c + "\n\n\a")

    list_sentence = text.split("\a")
    for sentence in list_sentence:
        print(sentence.strip(" "), end="")
