#!/usr/bin/python3
def weight_average(my_list=[]):
    a = 0
    ule = 0
    if my_list == []:
        return 0
    for i in range(0, len(my_list)):
        for j in range(0, 1):
            a = a + my_list[i][j] * my_list[i][j + 1]
            ule = ule + my_list[i][j + 1]
    a = a/ule
    return a
