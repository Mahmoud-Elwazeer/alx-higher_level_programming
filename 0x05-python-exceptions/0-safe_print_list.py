#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print("{}".format(i), end="")
        print()
        return (i)
    except ValueError:
        print("Failed\n")
