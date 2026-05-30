# ================================================
# Flight Price Manipulation Detector
# File 1: Data Loading & Exploration
# Author: [Your Name]
# ================================================

import pandas as pd


def load_data():
    """Load and explore the flight price dataset"""

    print("=" * 55)
    print("Loading Flight Price Dataset...")
    print("=" * 55)

    df = pd.read_csv("data/Clean_Dataset.csv")

    # drop unnamed index column
    df.drop(columns=['Unnamed: 0'], inplace=True)

    print(f"\nDataset shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nFirst look:")
    print(df.head())

    print(f"\nMissing values:")
    print(df.isnull().sum())

    print(f"\nAirlines in dataset:")
    print(df['airline'].value_counts())

    print(f"\nSource cities:")
    print(df['source_city'].unique())

    print(f"\nFlight classes:")
    print(df['class'].value_counts())

    print("\n✅ Data loaded successfully!")
    return df


if __name__ == "__main__":
    df = load_data()
