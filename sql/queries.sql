-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM dim_fund
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per month
SELECT strftime('%Y-%m',date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- Transactions by state
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense ratio < 1%
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top fund houses
SELECT fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Risk category count
SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- Average return by category
SELECT category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

-- Monthly inflows
SELECT *
FROM fact_aum;

-- Top performing funds
SELECT scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC;

-- Sharpe ratio ranking
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC;
