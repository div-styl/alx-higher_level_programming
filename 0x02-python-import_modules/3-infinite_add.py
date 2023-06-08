#!/usr/bin/python3
if __name__ == '__main__':
    """
    this program do the job of addition of one number
    and more. the numbers are taken in method of argv
    """
import sys
argvlen = len(sys.argv) - 1
sum = 0
if argvlen >= 1:
    for i in range(1, argvlen + 1):
        sum += int(sys.argv[i])
print('{}'.format(sum))
