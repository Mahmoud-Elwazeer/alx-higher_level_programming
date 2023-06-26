#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        size = 0
        for i in my_list[:x]:
            size++
            print("{}".format(i), end="")
        print()
        return (size)
    except ValueError:
        print("Failed\n")
