#!/usr/bin/python3
def uppercase(str):
    upc = ""
    i = 0
    while i < len(str):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            upp = chr(ord(str[i]) - ord('a') + ord('A'))
            upc += upp
        else:
            upc += str[i]
        i += 1
    print('{}'.format(upc))
