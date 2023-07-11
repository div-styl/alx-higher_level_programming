#!/usr/bin/python3
"""define func write_file"""


def write_file(filename="", text=""):
    """return a number of characters written in text"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
