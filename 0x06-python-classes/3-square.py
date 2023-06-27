#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represntation of class"""
    def __init__(self, size=0):
        """init the Square
        Args:
            size: the numnber square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ init the area func"""
        return (self.__size * self.__size)
