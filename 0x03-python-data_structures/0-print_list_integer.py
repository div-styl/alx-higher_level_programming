#!/usr/bin/python3
if __name__ == "__main__":
    """function print all the number of list"""
    def print_list_integer(my_list=[]):
        for numbers in my_list:
            if isinstance(numbers, int):
                print('{}'.format(numbers))

    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
