#!/usr/bin/python3
""" matrix_divided """


def matrix_divided(matrix, div):
    """ Divide each element of a matrix by dev """

    m = []
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        else:
            m.append(len(i))
        for x in i:
            if type(x) is not float and type(x) is not int:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if len(set(m)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) is float or type(div) is int:
        pass
    else:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(x/div, 2) for x in j] for j in matrix]
