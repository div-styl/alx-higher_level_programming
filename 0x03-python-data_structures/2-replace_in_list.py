#!/usr/bin/python3
if __name__ == "__main__":
    """
    function that replaces an element of a
    list at a specific position (like in C).
    """
    def replace_in_list(my_list, idx, element):
        len_list = len(my_list)
        if idx < 0 or idx >= len_list:
            return (my_list)
        my_list[idx] = element
