#!/usr/bin/python3
if __name__ == '__main__':
    """get the index of list"""
    def element_at(my_list, idx):
        range_list = len(my_list)
        if idx < 0 or idx >= range_list:
            return (None)
        return (my_list[idx])
