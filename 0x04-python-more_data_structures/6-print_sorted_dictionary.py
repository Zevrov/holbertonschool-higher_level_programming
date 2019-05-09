#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for items in sorted(a_dictionary):
        print("%s: %s" % (items, a_dictionary[items]))
