#!/usr/bin/python3
""" defines a function to print pascal triangle """


def pascal_triangle(n):
    """ loop through n """

    lis = []
    for row in range(n):
        if row == 0:
            ls_row = [1]
        else:
            ls_row = []
        for el in range(row):
            if el == 0:
                ls_row.append(1)
            if el > 0 and el < row:
                ls_row.append(lis[row-1][el]+lis[row-1][el-1])
            if el == row - 1:
                ls_row.append(1)

        lis.append(ls_row)
    return lis
