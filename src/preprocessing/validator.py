import pandas as pd


def dataset_info(df):
    print("=" * 50)
    print("Dataset Shape:")
    print(df.shape)

    print("=" * 50)
    print("Columns:")
    print(df.columns)

    print("=" * 50)
    print("Data Types:")
    print(df.dtypes)

    print("=" * 50)
    print("Missing Values:")
    print(df.isnull().sum())

    print("=" * 50)
    print("Duplicate Rows:")
    print(df.duplicated().sum())

    print("=" * 50)
    print("Blank values in TotalCharges:")
    print((df["TotalCharges"] == " ").sum())

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    print("=" * 50)
    print("Data Types (After Conversion):")
    print(df.dtypes)

    print("=" * 50)
    print("Missing Values (After Conversion):")
    print(df.isnull().sum())