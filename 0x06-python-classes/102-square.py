#!/usr/bin/python3

"""
    Define Square Class
"""


class Square:
    """
    initialize Private instance attribute: using propery

    Aegs:
        size: 0 default
        position: 0, 0 default
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
    property for position
    """
    @property
    def position(self):
        return self._position

    """
    Set position value

    Args:
        value: value of position
    """
    @position.setter
    def position(self, value):
        if not self._check_tuple(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    """"
    check position must be a tuple of 2 positive integers

    Args:
        vakue: To check
    """
    def _check_tuple(self, value):
        flag = False
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    flag = True
        return (flag)
    """
    calc area of square
    """
    def area(self):
        return (self.size ** 2)

    """
    print area as shape
    """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            val = self.position[0] if self.position[0] > self.position[1] \
                    else self.position[1]
            for i in range(self.size):
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
    """
    when call the name of object
    """
    def __str__(self):
        return self.area()
