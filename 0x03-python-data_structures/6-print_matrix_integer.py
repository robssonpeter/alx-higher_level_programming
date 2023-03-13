#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        if matrix == [[]]:
            print("")
        for cell in row:
            if index < len(row) - 1:
                print("{:d}".format(cell), end=" ")
            else:
                print("{:d}".format(cell))
            index = index + 1
