#!/usr/bin/python3
"""define the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init rectangle

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle's position. Defaults to 0.
            y (int, optional): y-coordinate of the rectangle's position. Defaults to 0.
            id (int, optional): Unique ID of the rectangle. Defaults to None.
        """
        super().__init__(id)

        self._check_integer_parameter(width, 'width')
        self._check_integer_parameter(height, 'height')
        self._check_integer_parameter(x, 'x')
        self._check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle."""
        self._check_integer_parameter(value, 'width')
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """get the height of the rectangle."""
        self._check_integer_parameter(value, 'height')
        self.__height = value

    @property
    def x(self):
        """get the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """get the x-coordinate of the rectangle's position."""
        self._check_integer_parameter(value, 'x')
        self.__x = value

    @property
    def y(self):
        """get the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y-coordinate of the rectangle's position."""
        self._check_integer_parameter(value, 'y')
        self.__y = value

    def _check_integer_parameter(self, value, param):
        """
        check if a value is an integer and satisfies specific conditions.

        Args:
            value: The value to be checked.
            param (str): The name of the parameter being checked.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value does not meet the specified conditions.
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """display the rectangle using '#' characters."""
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """get a string representation of the rectangle."""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        argc = len(args)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargs:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """get a dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }