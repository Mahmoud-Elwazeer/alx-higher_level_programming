#!/usr/bin/python3

"""
 prints a text with 2 new lines after each of these: ., ? and :
"""


def text_indentation(text):
    """
    print new line after specific character

    Args:
        text: text
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print()
            print()
        elif i == " ":
            continue
        else:
            print(i, end="")
