#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ule = 0
    for i in my_list:
        try:
            if ule < x:
                print(i, end="")
                ule += 1
        except IndexError:
            pass
    print()
    return ule
