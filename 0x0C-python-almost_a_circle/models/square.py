#!/usr/bin/python3
"""define a class square inhereted from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """reprenstation of the class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """inti values"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrive the width"""
        return self.width

    @size.setter
    def size(self, value):
        """init value with width and height"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if args and len(args) != 0:
            counter = 0
            for arg in args:
                if counter == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if counter == 1:
                    self.size = arg
                elif counter == 2:
                    self.x = arg
                elif counter == 3:
                    self.y = arg
                counter += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """small dictionray returned"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
