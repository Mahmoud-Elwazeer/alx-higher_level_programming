#!/usr/bin/python3
"""
Define Rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initialize private instance
        """
        self.width = width
        self.height = height

    """ using property
    """
    @property
    def width(self):
        return self._width

    """ set value for width
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    """ use property
    """
    @property
    def height(self):
        return self._height

    """ set height of rectangle
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
