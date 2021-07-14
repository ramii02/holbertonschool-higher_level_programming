#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    num = 0
    len_n = roman_string
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    while num in range(num, len(len_n)):
        if num < len(len_n) - 1 and roman[len_n[num]] < roman[len_n[num + 1]]:
            value = value - roman[len_n[num]]
        else:
            value = value + roman[len_n[num]]
    return value
