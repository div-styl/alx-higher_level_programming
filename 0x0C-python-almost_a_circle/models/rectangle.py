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

    def area(self):
        """return the area of rectangle"""
        return self.height * self.width

    def display(self):
        """print the rectangle into stdoutput"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print('') for _ in range(self.y)]
        for he in range(self.height):
            [print(' ', end='') for _ in range(self.x)]
            [print('#', end='') for _ in range(self.width)]
            print('')

    def __str__(self):
        """informal printing of rectangle"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self. id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            counter = 0
            for arguments in args:
                if counter == 0:
                    if arguments is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arguments
                elif counter == 1:
                    self.width = arguments
                elif counter == 2:
                    self.height = arguments
                elif counter == 3:
                    self.x = arguments
                elif counter == 4:
                    self.y = arguments
                counter += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """small dictionary"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
