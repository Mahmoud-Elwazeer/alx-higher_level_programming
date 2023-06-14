#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        result = map(lambda x: x ** 2, matrix[i])
        new.append(list(result))
    return new
