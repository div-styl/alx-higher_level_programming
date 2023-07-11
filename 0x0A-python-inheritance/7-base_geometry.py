#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """represent base geometry"""

    def area(self):
        """Not yet implemented."""
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
