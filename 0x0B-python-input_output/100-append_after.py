#!/usr/bin/python3
"""
inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    insert depend on search
    """
    line_num = 0
    with open(filename, 'r', encoding="utf-8") as myfile:
        lines = myfile.readlines()
    with open(filename, 'w', encoding="utf-8") as myfile:
        for line in lines:
            myfile.write(line)
            if search_string in line:
                myfile.write(new_string)

    myfile.closed
