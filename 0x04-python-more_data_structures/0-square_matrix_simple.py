#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for mat in matrix:
        row = [x**2 for x in mat]
        new_matrix.append(row)
    return new_matrix
