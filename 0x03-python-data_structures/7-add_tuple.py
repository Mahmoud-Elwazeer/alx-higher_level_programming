#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = []
    for i in range(2):
        result = tuple_a[i] + tuple_b[i]
        tuple_sum.append(result)

    return tuple(tuple_sum)