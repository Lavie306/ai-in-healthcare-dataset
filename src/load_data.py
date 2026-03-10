import pandas as pd

def load_parquet(path):
    return pd.read_parquet(path)

def load_csv(path):
    return pd.read_csv(path)
