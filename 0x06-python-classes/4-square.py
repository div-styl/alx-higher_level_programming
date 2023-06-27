#!/usr/bin/python3
"""define a class square"""


class Square:
    """represent the class"""
    def __init__(self, size=0):
        """ init
        Args:
            size: the nw number of square
        """
        self.__size = size

    @property
    def size(self):
        """init func size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ init the func
        Args:
            value: a new value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the new square"""
        return (self.__size * self.__size)
