#!/usr/bin/python3
def safe_print_division(a, b):
    """
    function that do the arthamtic division
    Argu:
        a and b: are numbers
    Return:
        return the total sum if the division possible
        or None if not
    """
    try:
        sum = a / b
    except (TypeError, ZeroDivisionError):
        sum = None
    finally:
        print('Inside result: {}'.format(sum))
    return (sum)
