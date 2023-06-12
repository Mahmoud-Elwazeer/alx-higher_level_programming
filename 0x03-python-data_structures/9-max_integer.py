#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    result = my_list[0]
    for i in my_list:
        if result < i:
            result = i
    return (result)
