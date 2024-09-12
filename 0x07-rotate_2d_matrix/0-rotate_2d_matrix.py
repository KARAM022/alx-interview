#!/usr/bin/python3
"""_summary_
"""


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix
