#!/usr/bin/python3

def no_c(my_string):
    my_string = list(my_string)
    count = 0
    for i in my_string:
        if i == 'c':
            del my_string[count]
        elif i == 'C':
            del my_string[count]
        count += 1
    my_string = ''.join(my_string)
    return my_string
