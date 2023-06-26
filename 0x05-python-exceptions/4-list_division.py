#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(0, list_length):
        try:
            sum = my_list_1[x] / my_list_2[x]
        except (TypeError):
            print('wrong type')
            sum = 0
        except (ZeroDivisionError):
            print('division by 0')
            sum = 0
        except (IndexError):
            print('out of range')
            sum = 0
        finally:
            new_list.append(sum)
    return (new_list)
