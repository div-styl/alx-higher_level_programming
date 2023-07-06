#!/usr/bin/python3
"""define func"""


def magic_string():
    """funct print BestSchool in certain pattren"""
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ("BestSchool, " * (magic_string.count - 1) + "BestSchool")
