#!/usr/bin/env python3
"""Module that sorts a DataFrame by High price."""


def high(df):
    """Sorts the DataFrame by High in descending order."""
    return df.sort_values(by="High", ascending=False)
