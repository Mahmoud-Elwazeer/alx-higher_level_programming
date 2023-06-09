#!/usr/bin/python3
"""
reads a text file (UTF8) and prints it to stdou
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, 'r', encoding="utf-8") as myfile:
        for line in myfile:
            print(line, end="")

    myfile.closed
