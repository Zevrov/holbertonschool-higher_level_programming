#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool = []
    for z in my_list:
        if z % 2 == 0:
            bool.append(True)
        else:
            bool.append(False)
    return bool
