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

    delimiters = ['.', '?', ':']

    strt = 0

    for i, char in enumerate(text):
        if char in delimiters:
            print(text[strt:i + 1].strip())
            print()
            strt = i + 1

    if strt < len(text):
        print(text[strt:].strip())


if if __name__ == "__main__":
    text_indentation("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
    Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
    Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
    Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
    Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
    rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
    stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
    cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
    beatiorem! Iam ruinas videres
    """)
