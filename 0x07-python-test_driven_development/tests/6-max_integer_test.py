#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class test_max_integer(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_2(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
