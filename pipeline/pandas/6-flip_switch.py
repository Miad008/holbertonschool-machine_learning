#!/usr/bin/env python3
"""Module that reverses a DataFrame and transposes it."""


def flip_switch(df):
    """Sorts the DataFrame in reverse chronological order and transposes it."""
    return df.iloc[::-1].T
