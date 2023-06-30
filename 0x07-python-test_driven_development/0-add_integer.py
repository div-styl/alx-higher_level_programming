#!/usr/bin/python3
def add_integer(a, b=98):
    """do addition of two digits that aren't float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a is None  and b is None:
        return (None)
    return (int(a) + int(b))