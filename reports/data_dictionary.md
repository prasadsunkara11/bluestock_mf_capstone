# Data Dictionary

## 01_fund_master.csv

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| amfi_code          | Integer   | Unique AMFI Scheme Code |
| fund_house         | Text      | Mutual Fund Company     |
| scheme_name        | Text      | Scheme Name             |
| category           | Text      | Fund Category           |
| sub_category       | Text      | Sub Category            |
| plan               | Text      | Direct/Regular Plan     |
| launch_date        | Date      | Scheme Launch Date      |
| benchmark          | Text      | Benchmark Index         |
| expense_ratio_pct  | Float     | Expense Ratio (%)       |
| exit_load_pct      | Float     | Exit Load (%)           |
| min_sip_amount     | Integer   | Minimum SIP Amount      |
| min_lumpsum_amount | Integer   | Minimum Lumpsum Amount  |
| fund_manager       | Text      | Fund Manager Name       |
| risk_category      | Text      | Risk Category           |
| sebi_category_code | Text      | SEBI Category Code      |

---

## 02_nav_history.csv

| Column    | Data Type | Description     |
| --------- | --------- | --------------- |
| amfi_code | Integer   | Scheme Code     |
| date      | Date      | NAV Date        |
| nav       | Float     | Net Asset Value |

---

## 03_aum_by_fund_house.csv

| Column         | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting Date    |
| fund_house     | Text      | Mutual Fund House |
| aum_lakh_crore | Float     | AUM in Lakh Crore |
| aum_crore      | Integer   | AUM in Crore      |
| num_schemes    | Integer   | Number of Schemes |

---

## 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                 |
| ------------------------- | --------- | --------------------------- |
| month                     | Date      | Reporting Month             |
| sip_inflow_crore          | Integer   | SIP Inflow Amount           |
| active_sip_accounts_crore | Float     | Active SIP Accounts         |
| new_sip_accounts_lakh     | Float     | New SIP Accounts            |
| sip_aum_lakh_crore        | Float     | SIP Assets Under Management |
| yoy_growth_pct            | Float     | Year-over-Year Growth (%)   |

---

## 05_category_inflows.csv

| Column           | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Date      | Reporting Month   |
| category         | Text      | Fund Category     |
| net_inflow_crore | Float     | Net Inflow Amount |

---

## 06_industry_folio_count.csv

| Column              | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Date      | Reporting Month |
| total_folios_crore  | Float     | Total Folios    |
| equity_folios_crore | Float     | Equity Folios   |
| debt_folios_crore   | Float     | Debt Folios     |
| hybrid_folios_crore | Float     | Hybrid Folios   |
| others_folios_crore | Float     | Other Folios    |

---

## 07_scheme_performance.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | Scheme Code                   |
| scheme_name        | Text      | Scheme Name                   |
| fund_house         | Text      | Fund House                    |
| category           | Text      | Category                      |
| plan               | Text      | Plan Type                     |
| return_1yr_pct     | Float     | 1-Year Return (%)             |
| return_3yr_pct     | Float     | 3-Year Return (%)             |
| return_5yr_pct     | Float     | 5-Year Return (%)             |
| benchmark_3yr_pct  | Float     | Benchmark Return              |
| alpha              | Float     | Alpha Metric                  |
| beta               | Float     | Beta Metric                   |
| sharpe_ratio       | Float     | Sharpe Ratio                  |
| sortino_ratio      | Float     | Sortino Ratio                 |
| std_dev_ann_pct    | Float     | Annualized Standard Deviation |
| max_drawdown_pct   | Float     | Maximum Drawdown              |
| aum_crore          | Integer   | Assets Under Management       |
| expense_ratio_pct  | Float     | Expense Ratio                 |
| morningstar_rating | Integer   | Morningstar Rating            |
| risk_grade         | Text      | Risk Grade                    |

---

## 08_investor_transactions.csv

| Column             | Data Type | Description             |
| ------------------ | --------- | ----------------------- |
| investor_id        | Text      | Investor Identifier     |
| transaction_date   | Date      | Transaction Date        |
| amfi_code          | Integer   | Scheme Code             |
| transaction_type   | Text      | SIP/Lumpsum/Redemption  |
| amount_inr         | Integer   | Transaction Amount      |
| state              | Text      | State                   |
| city               | Text      | City                    |
| city_tier          | Text      | T30/B30 Classification  |
| age_group          | Text      | Investor Age Group      |
| gender             | Text      | Investor Gender         |
| annual_income_lakh | Float     | Annual Income           |
| payment_mode       | Text      | Payment Method          |
| kyc_status         | Text      | KYC Verification Status |

---

## 09_portfolio_holdings.csv

| Column            | Data Type | Description             |
| ----------------- | --------- | ----------------------- |
| amfi_code         | Integer   | Scheme Code             |
| stock_symbol      | Text      | Stock Ticker            |
| stock_name        | Text      | Company Name            |
| sector            | Text      | Sector                  |
| weight_pct        | Float     | Portfolio Weight (%)    |
| market_value_cr   | Float     | Market Value (Crore)    |
| current_price_inr | Float     | Current Share Price     |
| portfolio_date    | Date      | Portfolio Snapshot Date |

---

## 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading Date         |
| index_name  | Text      | Benchmark Index Name |
| close_value | Float     | Closing Index Value  |

---
