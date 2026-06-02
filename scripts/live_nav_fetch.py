import requests
import pandas as pd
from pathlib import Path

# Create raw data folder if it doesn't exist
raw_path = Path("data/raw")
raw_path.mkdir(parents=True, exist_ok=True)

# Mutual Fund Schemes
funds = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in funds.items():
    try:
        print(f"Fetching {fund_name}...")

        url = f"https://api.mfapi.in/mf/{scheme_code}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = raw_path / f"{fund_name}.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")

    except Exception as e:
        print(f"Error fetching {fund_name}: {e}")

print("\nAll NAV files downloaded successfully!")