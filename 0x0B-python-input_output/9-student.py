#!/usr/bin/python3
"""define a class student"""


class Student:
    """represent the class student"""
    def __init__(self, first_name, last_name, age):
        """init values in the argumen func"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        func that retrieves a dictionary
        representation of a Student
        """
        return self.__dict__.copy()
