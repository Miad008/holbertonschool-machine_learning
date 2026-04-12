#!/usr/bin/env python3
"""Module that sets Timestamp as index."""


def index(df):
    """Sets the Timestamp column as the index."""
    return df.set_index("Timestamp")
