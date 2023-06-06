#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ''
    for i in str:
        if i != n:
            newstring += str[i]
        i += 1
    return newstring
