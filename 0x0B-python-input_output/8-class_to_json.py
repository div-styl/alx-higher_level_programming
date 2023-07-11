#!/usr/bin/python3
"""define a class class_to_json"""


def class_to_json(obj):
    """represent a class to json"""
    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
