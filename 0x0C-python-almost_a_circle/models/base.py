#!/usr/bin/python3
"""define the class base"""


class Base:
    """
    represent the class Base
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """init the value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

