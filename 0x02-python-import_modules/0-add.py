#!/usr/bin/python3

a = 1
b = 2

add = __import__('add_0').add

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
