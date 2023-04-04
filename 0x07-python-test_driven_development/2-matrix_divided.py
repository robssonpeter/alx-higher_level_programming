#!/usr/bin/python3

def matrix_divided(matrix, div):
    types =  [type(1), type(1.2)]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) not in types:
        raise TypeError('div must be a number')
    length = len(matrix[0])
    div_matrix = []
    for row in matrix:
        if type(row) != type([1]):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        elif length != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for element in row:
            if type(element) not in types:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        div_row =  [round(x/div, 2) for x in row]
        div_matrix.append(div_row)

    return div_matrix

