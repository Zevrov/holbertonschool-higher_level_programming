#!/usr/bin/python3
def fizzbuzz():
    for z in range (1, 101):
        if z % 15 == 0:
            print('FizzBuzz ', end='')
        elif z % 5 == 0:
            print('Buzz ', end='')
        elif z % 3 == 0:
            print('Fizz ', end='')
        else
            print('{} '.format(z), end='')
