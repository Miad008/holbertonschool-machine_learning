#!/usr/bin/env python3
import pandas as pd
import string

def from_numpy(array):
    cols = array.shape[1]
    labels = list(string.ascii_uppercase[:cols])
    return pd.DataFrame(array, columns=labels)
