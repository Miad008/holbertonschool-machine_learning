#!/usr/bin/env python3
"""Convert DataFrame to NumPy array"""


def array(df):
    """Return last 10 rows of High and Close"""
    return df[['High', 'Close']].tail(10).to_numpy()
