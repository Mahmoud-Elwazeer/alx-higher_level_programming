#!/usr/bin/python3

"""
    Example:
    >>> add_integer(100, 2)
    102
"""


def add_integer(a, b=98):
    """
    add Two integer
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
