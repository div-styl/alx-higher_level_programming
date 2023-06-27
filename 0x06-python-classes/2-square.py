#!/usr/bin/python3
"""Define a square"""


class Square:
    """the represtation of class"""
    def __init__(self, size=0):
        """ initilaze the Square
        Args:
        size: the new size of the square
        """
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
