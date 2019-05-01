#!/usr/bin/python3
def uppercase(str):
    leng = len(str)
    for z in range(0, leng):
        x = str[z]
        if ord(x) <= ord('z') and ord(z) >= ord('a'):
            x = chr(ord(x) - 32)
        print('{}'.format(x), end='')
    print()
