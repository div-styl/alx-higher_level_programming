#!/usr/bin/python3
if __name__ == '__main__':
    """count the number of arguments if there is one"""
import sys
"""
get the len of the arguments 1st and then set condi
the -1 can be consider as an overwrite of arguments counter
the name of program consider as 0 and 1st argu is 1
therefor the -1 ghost the name of program and convert
the 1st arguments from value one to zero
"""
argucnt = len(sys.argv) - 1
# our condi that will demonstaret our program
if argucnt == 0:
    print('{} arguments.'.format(argucnt))
elif argucnt == 1:
    print('1 argument: ')
    print('1: {}'.format(sys.argv[1]))
else:
    print('{} arguments:'.format(argucnt))
    for i in range(1, argucnt + 1):
        print('{}: {}'.format(i, sys.argv[i]))
