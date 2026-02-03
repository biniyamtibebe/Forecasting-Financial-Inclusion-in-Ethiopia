# src/data_loader.py

import pandas as pd

DATE_COL = "observation_date"

def load_unified_data(path: r"c:\Users\hp\Pictures\Forecasting Financial Inclusion in Ethiopia\Forecasting-Financial-Inclusion-in-Ethiopia\data\raw\ethiopia_fi_unified_data.csv") -> pd.DataFrame:
    """
    Load unified Ethiopia financial inclusion dataset
    and apply basic schema checks.
    """
    df = pd.read_csv(path)

    required_cols = [
        "record_type",
        "indicator_code",
        "pillar",
        "value_numeric",
        DATE_COL,
        "confidence"
    ]

    missing = set(required_cols) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")
    df["year"] = df[DATE_COL].dt.year

    return df


def split_by_record_type(df: pd.DataFrame):
    """
    Split unified dataset into logical components.
    """
    observations = df[df["record_type"] == "observation"].copy()
    events = df[df["record_type"] == "event"].copy()
    targets = df[df["record_type"] == "target"].copy()
    impact_links = df[df["record_type"] == "impact_link"].copy()

    return observations, events, targets, impact_links
