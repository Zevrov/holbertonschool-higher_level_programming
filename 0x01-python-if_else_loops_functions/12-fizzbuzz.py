#!/usr/bin/python3
def fizzbuzz():
    for z in range(1, 101):
        if z % 3 == 0 and z % 5 == 0:
            print('FizzBuzz ', end='')
        elif z % 5 == 0:
            print('Buzz ', end='')
        elif z % 3 == 0:
            print('Fizz ', end='')
        else:
            print('{:d} '.format(z), end='')
