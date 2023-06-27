#!/usr/bin/python3

"""
    Define Square Class
"""


class Square:
    """
    initialize Private instance attribute: using propery

    Aegs:
        size
    """
    def __init__(self, size=0):
        self.size = size

    """
    Using property to private instance

    Arge:
        size: size of square
    """
    @property
    def size(self):
        return self._size

    """
    Set value for size

    Arge:
        value: value of size
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self._size = value

    """
    calc area of square
    """
    @property
    def area(self):
            return (self.size ** 2)
