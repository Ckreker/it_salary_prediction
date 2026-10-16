import pandas as pd


def check_quality(df):
    """Проверка качества данных (R1-R5)."""
    issues = []
    if df["Ids"].duplicated().any():
        issues.append(f"R1: дубликаты Ids: {df['Ids'].duplicated().sum()}")
    salary = pd.to_numeric(df["Salary"], errors="coerce")
    if (salary <= 0).any():
        issues.append(f"R2: Salary <= 0: {(salary <= 0).sum()}")
    both = df.dropna(subset=["From", "To"])
    if (both["From"] > both["To"]).any():
        issues.append(f"R3: From > To: {(both['From'] > both['To']).sum()}")
    if df["Description"].isna().any():
        issues.append(f"R4: пустой Description: {df['Description'].isna().sum()}")
    dates = pd.to_datetime(df["Published at"], errors="coerce", utc=True)
    if (dates > pd.Timestamp.utcnow()).any():
        issues.append("R5: даты в будущем")
    return issues
