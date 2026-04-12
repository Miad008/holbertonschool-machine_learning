#!/usr/bin/env python3
"""Module that computes descriptive statistics."""


def analyze(df):
    """Computes statistics excluding Timestamp."""
    df = df.drop(columns=["Timestamp"], errors="ignore")
    return df.describe()
