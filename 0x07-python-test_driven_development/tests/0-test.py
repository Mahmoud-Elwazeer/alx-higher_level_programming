import unittest

add_integer = __import__('0-add_integer').add_integer

class test_add_integer(unittest.TestCase):
    def test_add_positive(self):
		# Test when add positive numbers
    	self.assertEqual(add_integer(20, 30), 50)

    def test_add_negative(self):
		#Test when add negative number
    	self.assertEqual(add_integer(-1, -3), -4)

    def test_zero(self):
	    # Test Zero Result
        self.assertEqual(add_integer(1, -1), 0)

    def test_type_1(self):
		# Test Type value
        self.assertRaises(TypeError, add_integer, "str", "str")

    def test_type_2(self):
                # Test Type value
        self.assertRaises(TypeError, add_integer, True, True)

    def test_type_3(self):
                # Test Type value
        self.assertRaises(TypeError, add_integer, 3 + 5j, 2 + 3j)
