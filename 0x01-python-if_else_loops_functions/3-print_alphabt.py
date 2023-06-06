#!/usr/bin/python3
r = ''
for i in range(97, 122 + 1):
    if i == 101 or i == 113:
        continue
    r += chr(i)
print('{}'.format(r), end='')
# print(r.format(*r), end='')
