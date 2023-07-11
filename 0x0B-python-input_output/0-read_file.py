#!/usr/bin/python3
"""functio to read a file"""


def read_file(filename=""):
    """
    open adn read a file func taking a filename as argument
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
