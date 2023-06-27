#!/usr/bin/python3

"""
    Define Class Square
"""


class Square:
    """
    Initialize Private instance attribute

    Args:
        size (int): integer value > 0
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
