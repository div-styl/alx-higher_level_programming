#!/usr/bin/python3
def uppercase(str):
    upc = ""
    i = 0
    while i < len(str):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            upp = chr(ord(str[i]) - 32)
            upc += upp
        i += 1
    print('{}'.format(upc))
