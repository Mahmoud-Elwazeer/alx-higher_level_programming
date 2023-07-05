#!/usr/bin/python3

"""
add integers
"""


def add_integer(a, b=98):
    """
    add Two integer
    Args:
        a (int): 1st number
        b (int): 2nd number
    Returns:
        a + b
    """
    if a is None:
        return (0)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
