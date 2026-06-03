import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")
processed_path.mkdir(exist_ok=True)

# NAV HISTORY
nav = pd.read_csv(raw_path/"02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill NAV
nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

# Keep only valid NAV
nav = nav[nav["nav"] > 0]

nav.to_csv(
    processed_path/"02_nav_history_clean.csv",
    index=False
)

print("NAV cleaned")


txn = pd.read_csv(
    raw_path/"08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

txn = txn[
    txn["transaction_type"].isin(valid_types)
]

txn = txn[
    txn["amount_inr"] > 0
]

valid_kyc = [
    "Verified",
    "Pending"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    processed_path/"08_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

perf = pd.read_csv(
    raw_path/"07_scheme_performance.csv"
)

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio check
perf = perf[
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
]

perf.to_csv(
    processed_path/"07_performance_clean.csv",
    index=False
)

print("Performance cleaned")