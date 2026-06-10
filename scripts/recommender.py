import pandas as pd

performance = pd.read_csv(
    "data/processed/07_performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

df = performance.merge(
    fund_master,
    on="amfi_code"
)

recommend = (
    df[df["risk_grade"] == risk]
    .sort_values(
        "sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print(df.columns.tolist())

print(
    recommend[
        [
            "scheme_name_x",
            "risk_grade",
            "sharpe_ratio"
        ]
    ]
)