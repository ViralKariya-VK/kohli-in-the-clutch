# src/data_loader.py

import pandas as pd
import os


def load_raw_data(filepath: str = "data/raw/matches.csv") -> pd.DataFrame:
    """
    Loads the raw match data from CSV.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw data not found at path: {filepath}")
    return pd.read_csv(filepath)


def load_cleaned_data(filepath: str = "data/processed/matches.csv") -> pd.DataFrame:
    """
    Loads the cleaned and processed match data.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Cleaned data not found at path: {filepath}")
    return pd.read_csv(filepath)


def get_data_summary(df: pd.DataFrame, name: str = "Dataset") -> None:
    """
    Prints quick summary: shape, nulls, dtypes
    """
    print(f"\nSummary of {name}")
    print("-" * 40)
    print(f"Shape: {df.shape}")
    print("\nColumn Types:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isnull().sum())


def filter_by_match_type(df: pd.DataFrame, match_type: str) -> pd.DataFrame:
    """
    Filter the dataset by match type (e.g., 'ODI', 'T20').
    """
    return df[df['match_type'].str.upper() == match_type.upper()]
