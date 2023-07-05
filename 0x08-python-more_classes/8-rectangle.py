#!/usr/bin/python3
"""
Define Rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        return (self._width * self.height)

    def perimeter(self):
        return (2 * (self._width + self._height))

    def __str__(self):
        result = []
        for i in range(self._height):
            r = []
            for j in range(self._width):
                r.append(Rectangle.print_symbol)
            r = "".join(r)
            result.append(r)
        result = "\n".join(result)
        return f"{result}"

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
