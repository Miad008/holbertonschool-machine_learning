#!/usr/bin/env python3
"""Module that removes rows with NaN values in Close column."""


def prune(df):
    """Removes entries where Close has NaN values."""
    return df.dropna(subset=["Close"])
