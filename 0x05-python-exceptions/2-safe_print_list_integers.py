#!/usr/bin/python3

'''
def safe_print_list_integers(my_list=[], x=0):
    try:
        size = 0
        for i in my_list[:x]:
            if (isinstance(i, int)):
                size += 1
                print("{:d}".format(i), end="")
        print()
        return (size)
    except IndexError as err:
        print("list index out of range", err)
'''


def safe_print_list_integers(my_list=[], x=0):
    try:
        size = 0
        for i in my_list[:x]:
            if (isinstance(i, int)):
                size += 1
                print("{:d}".format(i), end="")
        print()
        return (size)
    except IndexError as err:
        print(err)
