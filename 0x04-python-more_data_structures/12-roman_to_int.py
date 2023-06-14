#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    value = list(roman_string)
    result = 0
    for i in value:
        result += roman[i]

    return result
