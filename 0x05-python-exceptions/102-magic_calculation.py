#!/usr/bin/python3
def magic_calculation(a, b):
    magic = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                magic += a ** b / i
        except:
            magic = b + a
            break
    return magic
