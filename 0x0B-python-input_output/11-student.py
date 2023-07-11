#!/usr/bin/python3
""" define a class student"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            j_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        j_list[satr] = obj[satr]
            return j_list

        return obj

    def reload_from_json(self, json):
        """replace all attributes of the std instance"""
        for attri in json:
            self.__dict__[attri] = json[attri]