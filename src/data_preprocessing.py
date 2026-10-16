import pandas as pd


def clean(df):
    """Очистка данных."""
    df = df.drop_duplicates(subset=["Ids"]).copy()
    for col in ["From", "To", "Salary"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["Keys"] = df["Keys"].fillna("[]")
    df["Description"] = df["Description"].fillna("")
    return df.reset_index(drop=True)
