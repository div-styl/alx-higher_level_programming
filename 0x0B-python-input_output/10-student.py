#!/usr/bin/python3
"""define a class student"""


class Student:
    """represent the class student"""
    def __init__(self, first_name, last_name, age):
        """init values in the argumen func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        func that retrieves a dictionary
        representation of a Student
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            j_list = {}
            for atr in range(len(attrs)):
                for tar in obj:
                    if attrs[atr] == tar:
                        j_list[tar] = obj[atr]
            return j_list
        return obj
