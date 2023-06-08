#!/usr/bin/python3

def add(a, b):
    """My addition function

    Args:
        a: 1st number
        b: 2nd number

    Return:
        a + b
    """
    return (a + b)

a = 1
b = 2

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
