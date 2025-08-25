import pandas as pd
from sklearn.preprocessing import StandardScaler

def fill_missing_median(df):
    """
    Fill missing values in numeric columns using the median of each column.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with missing values filled.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)

    return df

def drop_missing(df, thresh=0.5):
    """
    Drop columns with too many missing values.

    Args:
        df (pd.DataFrame): Input DataFrame.
        thresh (float): Maximum allowed missing value ratio (default is 0.5).

    Returns:
        pd.DataFrame: A new DataFrame with columns dropped.
    """
    df = df.copy()
    min_non_na = int(len(df) * (1 - thresh))
    df = df.dropna(axis=1, thresh=min_non_na)
    return df

# Assume data distribution follows normal distribution
def normalize_data(df):
    """
    Normalize numeric columns using standard score (z-score) scaling.

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: A new DataFrame with normalized numeric features.
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include="number").columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df