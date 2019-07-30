#!/usr/bin/python3
def no_c(my_string):
    remove_c = ""
    for index in range(len(my_string)):
        if (my_string[index] != 'c' and my_string[index] != 'C'):
            remove_c += my_string[index]
    return remove_c
