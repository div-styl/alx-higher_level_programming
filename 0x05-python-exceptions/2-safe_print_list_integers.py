#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0;
    for i in range(x):
        try:
            value = my_list[i]
            print('{}'.format(int(value)), end='')
            counter += 1
        except (IndexError, TypeError):
            break
    print()
    return(counter)


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]

nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))