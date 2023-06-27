#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        rst = fct(*args)
        return (rst)
    except (IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
