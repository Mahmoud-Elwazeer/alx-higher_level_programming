#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    size = len(new_list)
    if 0 <= idx <= size - 1:
        new_list[idx] = element
    return (new_list)
