#!/usr/bin/python3
def no_c(my_string):
    remove_c = []
    for z in my_string:
        if z != 'C' or z != 'c':
            remove_c.append(z)
    return ''.join(remove_c)
