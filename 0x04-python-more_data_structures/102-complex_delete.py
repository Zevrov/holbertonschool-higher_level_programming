#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for index in list(a_dictionary.keys()):
        if a_dictionary[index] is value:
            del a_dictionary[index]
    return a_dictionary
