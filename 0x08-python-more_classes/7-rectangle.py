#!/usr/bin/python3
"""init class"""


class Rectangle:
    """represntation of the class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init the values"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return itself"""
        return self.__width

    @width.setter
    def width(self, value):
        """the func tha define the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return itself"""
        return self.__height

    @height.setter
    def height(self, value):
        """func the define the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the Rectangle"""
        return self.__height * self.width

    def perimeter(self):
        """return the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """printing the #"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                    for _ in range(self.__width)]) for _ in range(self.__height)]))

    def __repr__(self):
        """print the origin cause"""
        empty_string = "Rectangle(" + str(self.__width)
        empty_string += ", " + str(self.__height) + ")"
        return empty_string

    def __del__(self):
        """deletion of the rectangles"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
