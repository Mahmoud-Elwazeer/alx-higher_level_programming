#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    append string
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        myfile.write(text)

    myfile.closed
    return (len(text))
