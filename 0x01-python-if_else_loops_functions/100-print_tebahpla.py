#!/usr/bin/python3
aux = 0
for i in range(122, 96, -1):
    if aux == 0:
        print("{:c}".format(i), end="")
        aux = 1
    else:
        print("{:c}".format(i - 32), end="")
        aux = 0
