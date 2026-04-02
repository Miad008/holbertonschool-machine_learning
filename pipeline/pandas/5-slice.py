#!/usr/bin/env python3
"""Slice DataFrame"""


def slice(df):
    """Return every 60th row of selected columns"""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']][::60]
