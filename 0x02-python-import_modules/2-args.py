#!/usr/bin/python3
if __name__ == '__main__':
    """count the number of arguments that are given by user"""
import sys
len_arg = len(sys.argv) - 1
if len_arg == 0:
    print('{} argument.'.format(len_arg))
elif len_arg == 1:
    print('1 argument: ')
else:
    print('{} arguments: '.format(len_arg))
for i in range(1, len_arg + 1):
    print('{}: {}'.format(i, sys.argv[i]))
