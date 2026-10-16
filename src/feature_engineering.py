import pandas as pd


EXPERIENCE_MAP = {
    "Нет опыта": 0,
    "От 1 года до 3 лет": 24,
    "От 3 до 6 лет": 54,
    "Более 6 лет": 84,
}


def build_features(df):
    """Инжиниринг признаков."""
    df = df.copy()
    df["avg_salary"] = df[["From", "To"]].mean(axis=1).fillna(df["Salary"])
    df["experience_months"] = df["Experience"].map(EXPERIENCE_MAP).fillna(0).astype(int)
    df["skills_count"] = df["Keys"].apply(
        lambda x: len(eval(x)) if isinstance(x, str) and x.startswith("[") else 0
    )
    df["is_remote"] = df["Schedule"].fillna("").str.contains("Удал", case=False).astype(int)
    df["desc_len"] = df["Description"].str.len()
    df["desc_words"] = df["Description"].str.split().apply(len)
    return df
