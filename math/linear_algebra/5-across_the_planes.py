#!/usr/bin/env python3
"""Module that adds two 2D matrices"""


def add_matrices2D(mat1, mat2):
    """adds two matrices element-wise"""

    if len(mat1) != len(mat2):
        return None

    new_matrix = []

    for i in range(len(mat1)):

        if len(mat1[i]) != len(mat2[i]):
            return None

        row = []

        for j in range(len(mat1[i])):
            row.append(mat1[i][j] + mat2[i][j])

        new_matrix.append(row)

    return new_matrix
