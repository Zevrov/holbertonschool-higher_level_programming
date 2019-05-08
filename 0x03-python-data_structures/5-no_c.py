#!/usr/bin/python3
def no_c(my_string):
    remove_c = list(mystring)
    for z in my_string:
        if z == 'C' or z == 'c':
            remove_c.remove(z)
    return ''.join(remove_c)
