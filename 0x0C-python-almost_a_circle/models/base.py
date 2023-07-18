#!/usr/bin/python3
"""
A model that contains a Base class to manage square and rectangle
"""

import json
import os.path


class Base:
    """
    Base class for managing the id attribute of all classes that inherit from it.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance with an id attribute.

        Args:
            id (int, optional): Unique ID of the instance. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_of_dicts):
        """
        convert a list of dictionaries to a JSON string.

        Args:
            list_of_dicts (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if not list_of_dicts or len(list_of_dicts) == 0:
            return '[]'
        return json.dumps(list_of_dicts)

    @classmethod
    def save_to_file(cls, list_of_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_of_objs (list): List of objects to be saved.

        Returns:
            int: Number of characters written to the file.
        """
        filename = cls.__name__ + '.json'
        json_attrs = [obj.to_dictionary() for obj in list_of_objs] if list_of_objs else None
        json_string = cls.to_json_string(json_attrs)
        
        with open(filename, mode='w', encoding='utf-8') as file:
            return file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries.
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class with the given dictionary attributes.

        Args:
            **dictionary: Dictionary with the attributes for the new instance.

        Returns:
            instance: New instance of the class.
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)

        elif cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + '.json'
        
        if not os.path.exists(filename):
            return []
        
        with open(filename, mode='r', encoding='utf-8') as file:
            json_data = cls.from_json_string(file.read())
            return [cls.create(**data) for data in json_data]
