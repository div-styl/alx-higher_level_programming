#!/usr/bin/python3
"""define the class base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0 or \
                list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json list of objcts into a file
        Args:
            list_objs: list of objects
        """
        file = cls.__name__ + ".json"
        list_objs = [o.to_dictionary() for o in list_objs]
        with open(file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if json_string is None or len(json_string) == 0 or \
                json_string == []:
            return []
        return json.loads(json_string)
