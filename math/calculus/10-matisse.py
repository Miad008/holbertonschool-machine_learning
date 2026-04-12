#!/usr/bin/env python3
"""Module for polynomial derivative"""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial"""

    if (not isinstance(poly, list) or len(poly) == 0 or
            not all(isinstance(x, (int, float)) for x in poly)):
        return None

    if len(poly) == 1:
        return [0]

    result = []

    for i in range(1, len(poly)):
        result.append(poly[i] * i)

    return result
