#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    """print a matrix of integers"""
    rows = len(matrix)
    colons = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, colons):
            if j == colons - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
