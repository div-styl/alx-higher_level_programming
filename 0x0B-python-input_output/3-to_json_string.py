#!/usr/bin/python3
"""define func to_json_string"""
import json


def to_json_string(my_obj):
    """return  the JSON as respresentation of the string obj"""
    return json.dumps(my_obj)
