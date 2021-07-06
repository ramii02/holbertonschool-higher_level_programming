#!/usr/bin/python3
def multiply_by_2(my_dict):  # dict comprentation
    return {key: value * 2 for key, value in my_dict.items()}
