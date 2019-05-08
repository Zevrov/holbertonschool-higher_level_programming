#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dup = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return dup
    else:
        dup[idx] = element
    return dup
