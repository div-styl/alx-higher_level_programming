#!/usr/bin/python3
"""define a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle class"""
    def __init__(self, width, height):
        """ init values
        Args:
            width (int): The width of the rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
