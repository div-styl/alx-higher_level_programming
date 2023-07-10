#!/usr/bin/python3
"""define a class"""


class BaseGeometry:
    """representation of a class"""
    def area(self):
        """function raise error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """func validate the value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater 
