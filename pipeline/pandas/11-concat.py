#!/usr/bin/env python3
"""Module that concatenates two DataFrames."""


import pandas as pd


def concat(df1, df2):
    """Concatenates df2 on top of df1 with proper indexing."""

    # import index function
    index = __import__('10-index').index

    # set index
    df1 = index(df1)
    df2 = index(df2)

    # filter df2
    df2 = df2[df2.index <= 1417411920]

    # concatenate with labels
    return pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
