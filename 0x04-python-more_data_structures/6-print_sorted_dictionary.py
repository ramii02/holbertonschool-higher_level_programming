#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict:
        for i in sorted(my_dict):
            print("{:s}: {}".format(i, my_dict[i]))
