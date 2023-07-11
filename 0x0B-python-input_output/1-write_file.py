#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and returns the number of characters
"""


def write_file(filename="", text=""):
    """
    write string in text file
    """
    with open(filename, 'w', encoding="utf-8") as myfile:
        myfile.write(text)

    myfile.closed
    return (len(text))
