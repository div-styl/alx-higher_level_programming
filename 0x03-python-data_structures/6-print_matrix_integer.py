#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print('{:d}'.format(elements), end=' ' if row[-1] else "")
        print()
