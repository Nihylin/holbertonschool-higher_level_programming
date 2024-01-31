#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [[idx ** 2 for idx in row] for row in matrix]
    return result
