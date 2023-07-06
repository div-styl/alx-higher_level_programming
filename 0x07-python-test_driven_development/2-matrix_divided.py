#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Division of the matrix.

    Checks if the matrix is a list and its elements are integers or floats,
    otherwise raises a TypeError.
    Checks the length of the matrix; if it is empty, raises a TypeError.
    Checks if div is an int or float; otherwise raises a TypeError.
    Checks if div is not equal to 0; otherwise raises a ZeroDivisionError.
    """

    # Check if the matrix is a list and its elements are integers or floats
    if not isinstance(matrix, list) or not all(isinstance (row, list) for row in matrix) \
            or not all(isinstance(elements, (int, float))
                       for row in matrix for elements in row):
        raise TypeError('matrix must be a matrix'
                        '(list of lists) of integers/floats')

    # Check if the matrix is not empty
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a non-empty matrix (list of lists)")

    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and return the result
    return [[round(element / div, 2) for element in row] for row in matrix]
