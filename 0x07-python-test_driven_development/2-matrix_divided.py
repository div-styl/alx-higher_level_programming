#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    division of the matrix
    check if the matrix is a list and its elements if they are integers or floats
    otherwise return TypeError
    check the len of the matrix if it is empty thn return TypeError
    check div if it is int or float otherwise return TypeError
    check if div is not equal to 0 otherwise return ZeroDivisionError
    """
    if (not isinstance(matrix, list) or matrix == [] or 
        not all(isinstance(row, list) for row in matrix) or
        not all ((isinstance(elements, int) or isinstance(elements, float)
        for elements in [numbers for row in matrix for numbers in row]))):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len (matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return([list(map(lambda y: round(y / div, 2), row)) for row in matrix])
