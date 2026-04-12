#!/usr/bin/env python3
"""Module that concatenates two DataFrames."""

import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenates df2 on top of df1 with proper indexing."""
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2.loc[:1417411920]

    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
