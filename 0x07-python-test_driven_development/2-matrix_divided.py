#!/usr/bin/python3

"""
 function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Args:
        matrix:  must be a list of lists of integers or floats
        div: must be a number (integer or float)

    Return:
        Returns a new matrix
    """
    size = len(matrix[0])

    for i in matrix:
        if len(i) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf'):
        r = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        return r

    result = []
    for i in matrix:
        aux = []
        for j in i:
            r = j / div
            aux.append(round(r, 2))
        result.append(aux)

    return result
