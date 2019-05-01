#!/usr/bin/python3
for z in range(0, 100):
    if z == 99:
        print(z)
    else:
        print('{}, '.format(format(z, '02d')), end='')
