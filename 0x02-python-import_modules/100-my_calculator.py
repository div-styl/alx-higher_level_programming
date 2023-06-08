#!/usr/bin/python3
if __name__ == '__main__':
    """small calculatore with argv method"""
    import sys
    from calculator_1 import add, sub, mul, div
    len_arg = len(sys.argv) - 1
    operators = ['+', '-', '*', '/']
    if len_arg == 0 or len_arg != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    op = sys.argv[2]
    if op not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == operators[0]:
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif op == operators[1]:
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif op == operators[2]:
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif op == operators[3]:
        print('{} / {} = {}'.format(a, b, div(a, b)))
