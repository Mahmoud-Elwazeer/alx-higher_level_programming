#!/usr/bin/python3

import sys
import calculator_1 as cal
def main():    
    size = len(sys.argv)
    check_size(size)
    check_op(str(sys.argv[2]))
    calc(int(sys.argv[1]), int(sys.argv[3]), sys.argv[2])

def calc(n1, n2, op):
    if op == '+':
        result = cal.add(n1, n2)
    elif op == '-':
        result = cal.sub(n1, n2)
    elif op == '*':
        result = cal.mul(n1, n2)
    elif op == '/':
        result = cal.div(n1, n2)

    print("{} {} {} = {}".format(n1, op, n2, result))


def check_op(a):
    if a != "+" and a != '-' and a != '*' and a != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

def check_size(a):
    if a != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)


if __name__ == "__main__":
    main()
