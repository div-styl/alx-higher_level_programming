#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rst = 0
    pre_v = 0

    for chara in reversed(roman_string):
        value = roman_dictionary.get(chara, 0)
        if value >= pre_v:
            rst += value
        else:
            rst -= value
        pre_v = value
    return rst
