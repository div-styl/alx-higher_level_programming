#!/usr/bin/python3
"""
returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is instance of a class
    returns False if the object is not an instance of a class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
