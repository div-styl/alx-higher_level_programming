#!/usr/bin/python3
"""define the class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """reprsent the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init the value"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def width(self):
        """return the width itself"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """function that set the value of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """reterive the value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value to rectangle"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """retrieve itself"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value
    
    @property
    def y(self):
        """retrieve itself"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value