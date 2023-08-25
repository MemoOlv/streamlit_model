import pandas as pd


def multiplier(df: pd.DataFrame, times: float):
    df["value"] = df.value * times
    return df
