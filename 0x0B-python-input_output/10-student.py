#!/usr/bin/python3
"""
class Student that defines a student
"""


class Student:
    """
    class for student
    """
    def __init__(self, first_name, last_name, age):
        """
        init data
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to json
        """
        if attrs is None:
            dic = {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                  }
            return (dic)
