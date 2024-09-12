#!/usr/bin/python3
''' Rotate 2D Matrix '''


def rotate_2d_matrix(matrix):
    ''' Rotate 2D Matrix '''
    len_matrix = len(matrix)
    new_matrix = [[0] * len_matrix for i in range(len_matrix)]
    print(new_matrix)

    matrix.reverse()
    for x in range(len_matrix):
        for y in range(len_matrix):
            new_matrix[x][y] = matrix[y][x]

    for i in range(len_matrix):
        matrix[i] = new_matrix[i]
