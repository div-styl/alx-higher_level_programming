#!/usr/bin/python3
"""define a func that adds attribute to object"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        attribute (string): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
