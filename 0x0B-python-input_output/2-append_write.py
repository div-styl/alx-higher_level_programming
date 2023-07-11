#!/usr/bin/python3
"""define func append_write"""


def append_write(filename="", text=""):
    """retunr the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
