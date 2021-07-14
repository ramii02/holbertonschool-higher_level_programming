#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return None
    else:
        ule = my_list[0]
        while i in my_list:
            if i > ule:
                ule = i
        return ule
