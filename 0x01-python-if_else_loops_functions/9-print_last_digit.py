#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number - number // 10 * 10
    if 0 < last_digit < 10 and number < 0:
        last_digit = 10 - last_digit

    print("{}".format(last_digit), end='')
    return last_digit
