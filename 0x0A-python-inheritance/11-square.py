#!/usr/bin/python3
"""
define BaseGoemtry class and rectangle as subclass
"""


class BaseGeometry:
    """representation of a class"""
    def area(self):
        """function raise error"""
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer greater than 0.
        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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

    def area(self):
        """ return the area"""
        return self.__width * self.__height

    def __str__(self):
        """print the rectangle"""
        return "[Rectangle] {:d}/{:d}.format(self.__width, self.__height)"


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

    def __str__(self):
        return "[Square]{:d}/{:d}".format(self.__size, self.__size)
