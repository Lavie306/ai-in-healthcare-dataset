import pandas as pd

def merge_datasets(dfs):

    merged = pd.concat(dfs, ignore_index=True)

    merged = merged.drop_duplicates(subset=["question", "answer"])

    return merged