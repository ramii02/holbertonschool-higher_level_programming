#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ule = a_dictionary.copy()
    for d in a_dictionary:
        value = a_dictionary[d] * 2
        ule.update({d: value})
    return ule
