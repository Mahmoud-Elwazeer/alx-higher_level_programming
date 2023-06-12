#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = []
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    len_b = len(tuple_b)
    len_a = len(tuple_a)
    if len_a == 0:
        tuple_a.append(0)
        tuple_a.append(0)
    elif len_a == 1:
        tuple_a.append(0)
    if len_b == 0:
        tuple_b.append(0)
        tuple_b.append(0)
    elif len_b == 1:
        tuple_b.append(0)
    for i in range(2):
        result = tuple_a[i] + tuple_b[i]
        tuple_sum.append(result)

    return tuple(tuple_sum)
