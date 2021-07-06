#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        while i in range(0, len(matrix)):
            while z in range(0, len(matrix[i])):
                print("{:d}".format(matrix[i][z]), end="")
                if z != (len(matrix[i]) - 1):
                    print(" ", end="")
            print("")
