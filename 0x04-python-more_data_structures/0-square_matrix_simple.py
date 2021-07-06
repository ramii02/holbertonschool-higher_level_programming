#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    field = []
    fields = []
    for i in range(0, len(matrix)):
        field = []
        for j in range(0, len(matrix[0])):
            x = matrix[i][j]**2
            field.append(x)
        fields.append(field)
    return fields
