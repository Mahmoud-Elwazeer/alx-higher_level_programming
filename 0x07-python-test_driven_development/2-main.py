#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)
print(matrix)

