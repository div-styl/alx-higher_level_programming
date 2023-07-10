#!/usr/bin/python3
"""
class BaseGeometry and square as subclass
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """reprsentation of the class """
    def __init__(self, size):
        """init value size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area of square"""
        return self.__size ** 2
