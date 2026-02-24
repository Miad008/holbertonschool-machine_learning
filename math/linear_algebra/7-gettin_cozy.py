#!/usr/bin/env python3
"""Concatenate 2D matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a specific axis"""

    if axis == 0:
        # لازم عدد الأعمدة يكون نفسه
        if len(mat1[0]) != len(mat2[0]):
            return None

        # نرجع matrix جديدة
        new_matrix = [row[:] for row in mat1]
        new_matrix += [row[:] for row in mat2]
        return new_matrix

    if axis == 1:
        # لازم عدد الصفوف يكون نفسه
        if len(mat1) != len(mat2):
            return None

        new_matrix = []
        for i in range(len(mat1)):
            new_matrix.append(mat1[i][:] + mat2[i][:])

        return new_matrix

    return None
