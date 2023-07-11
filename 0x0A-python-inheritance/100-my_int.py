#!/usr/bin/python3
"""def class method"""


class MyInt(int):
    """represent a class"""
    def __eq__(self, other):
        """convert equality from none equals to equality"""
        return self.real != other

    def __ne__(self, other):
        """convert equality to none equality"""
        return self.real == other
