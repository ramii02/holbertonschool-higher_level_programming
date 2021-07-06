#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        ule1 = list(map(lambda x: x[0] * x[1], my_list))
        ule2 = list(map(lambda y: y[1], my_list))
        return sum(ule1) / sum(ule2)
    return
