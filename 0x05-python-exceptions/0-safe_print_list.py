#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list[i]:
        try:
            print("{:d}".format(i))
        except:
            pass
