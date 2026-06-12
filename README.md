# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, market trends, and portfolio risk. The project includes data ingestion, cleaning, storage, exploratory data analysis, advanced financial analytics, and interactive dashboard development using Power BI.

The objective is to provide meaningful insights into mutual fund investments through data-driven analysis and visualization.

---

## Project Objectives

* Build a robust ETL pipeline for mutual fund data.
* Clean and validate multiple financial datasets.
* Design and implement a SQLite data warehouse.
* Perform exploratory data analysis (EDA).
* Compute mutual fund performance metrics.
* Conduct advanced risk and portfolio analytics.
* Develop an interactive Power BI dashboard.
* Generate actionable business insights.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* SQLite
* SQLAlchemy
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
bluestock_mf_capstone/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── load_to_sqlite.py
│   ├── recommender.py
│   ├── live_nav_fetch.py
│   └── amfi_validation.py
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── screenshots/
│
├── reports/
│   ├── Final_Report.pdf
│   ├── var_cvar_report.csv
│   └── rolling_sharpe_chart.png
│
├── run_pipeline.py
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

Additional live NAV data was collected using MFAPI.

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/prasadsunkara11/bluestock_mf_capstone.git
cd bluestock_mf_capstone
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the ETL Pipeline

### Data Ingestion

```bash
python scripts/data_ingestion.py
```

### Data Cleaning

```bash
python scripts/data_cleaning.py
```

### Load Data into SQLite

```bash
python scripts/load_to_sqlite.py
```

### Run Complete Pipeline

```bash
python run_pipeline.py
```

---

## Exploratory Data Analysis

Open and run:

```text
notebooks/EDA_Analysis.ipynb
```

Key analyses include:

* NAV Trends
* AUM Growth
* SIP Inflow Analysis
* Investor Demographics
* Geographic Distribution
* Correlation Analysis

---

## Performance Analytics

Implemented metrics:

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard

Notebook:

```text
notebooks/Performance_Analytics.ipynb
```

---

## Advanced Analytics

Implemented models:

* Value at Risk (VaR)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* HHI Concentration Analysis
* Fund Recommendation System

Notebook:

```text
notebooks/05_advanced_analytics.ipynb
```

---

## Dashboard

Power BI Dashboard Pages:

### Industry Overview

* Total AUM
* SIP Inflows
* Folios
* Industry Trends

### Fund Performance

* Return vs Risk Analysis
* Fund Scorecard
* NAV Trends

### Investor Analytics

* Demographic Analysis
* State-wise Investments
* Transaction Insights

### SIP & Market Trends

* SIP Growth
* Category Inflows
* Market Comparison

Dashboard File:

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

## Key Findings

* SIP participation increased significantly during the study period.
* Large-cap funds delivered stable long-term performance.
* Risk-adjusted returns varied across schemes.
* Investor participation was concentrated in major states.
* High Sharpe Ratio funds consistently outperformed peers.
* Portfolio concentration differed significantly across funds.

---

## Future Enhancements

* Real-time market data integration.
* Machine learning-based recommendation engine.
* Portfolio optimization models.
* Automated report generation.
* Web application deployment.

---

## Author

Prasad Sunkara

B.Tech Computer Science Engineering

GitHub:
https://github.com/prasadsunkara11/bluestock_mf_capstone

---

## License

This project was developed as part of the Bluestock Mutual Fund Analytics Capstone Project for educational and learning purposes.
