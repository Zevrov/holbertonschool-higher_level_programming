#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        math = a / b
    except ZeroDivisionError:
        math = None
    finally:
        print("Inside result: {}".format(math))
        return (math)
