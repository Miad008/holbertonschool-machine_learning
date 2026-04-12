#!/usr/bin/env python3
"""Module for polynomial integral"""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial"""

    if (not isinstance(poly, list) or
            not all(isinstance(x, (int, float)) for x in poly) or
            not isinstance(C, int)):
        return None

    result = [C]

    for i in range(len(poly)):
        val = poly[i] / (i + 1)

        if val == int(val):
            val = int(val)

        result.append(val)

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
