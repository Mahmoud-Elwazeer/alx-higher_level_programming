#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number - number // 10 * 10

if last_digit < 10 and number < 0:
    last_digit = last_digit - 10

if last_digit < 6 and last_digit != 0:
    print("Last digit of %d is %d and is less than 6\
            and not 0" % (number, last_digit))
elif last_digit > 5 and last_digit != 0:
    print("Last digit of %d is %d and is greater than 5\
            and not 0" % (number, last_digit))
else:
    print("Last digit of %d is %d and is 0" % (number, last_digit))
