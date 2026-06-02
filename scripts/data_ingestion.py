import pandas as pd
from pathlib import Path
data_path = Path("data/raw")
csv_files = list(data_path.glob("*.csv"))
print(f"Found {len(csv_files)} files")
for file in csv_files:

    print("\n" + "="*60)

    print("Dataset:", file.name)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())