#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ule = []
    for a in range(0, len(my_list)):
        x = my_list[a]
        if x is search:
            x = replace
        ule.append(x)
    return ule
