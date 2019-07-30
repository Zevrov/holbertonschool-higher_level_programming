#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    num = 0
    sum = 0
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for index in reversed(roman_string):
        num = numbers[index]
        if sum < num * 5 else -num:
            sum += num
    return sum
