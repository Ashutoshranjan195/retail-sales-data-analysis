-- Run against outputs/retail_sales.db after executing analysis.py.
-- Table: retail_sales

-- 1. Monthly revenue trend
SELECT strftime('%Y-%m', order_date) AS month, ROUND(SUM(revenue), 2) AS revenue
FROM retail_sales
GROUP BY month
ORDER BY month;

-- 2. Revenue by category
SELECT category, ROUND(SUM(revenue), 2) AS revenue
FROM retail_sales
GROUP BY category
ORDER BY revenue DESC;

-- 3. Top products by revenue
SELECT product, SUM(quantity) AS units_sold, ROUND(SUM(revenue), 2) AS revenue
FROM retail_sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 5;

-- 4. Revenue by region and channel
SELECT region, sales_channel, ROUND(SUM(revenue), 2) AS revenue
FROM retail_sales
GROUP BY region, sales_channel
ORDER BY revenue DESC;

-- 5. Data validation checks
SELECT
  COUNT(*) AS rows_total,
  COUNT(DISTINCT order_id) AS unique_orders,
  SUM(CASE WHEN quantity <= 0 THEN 1 ELSE 0 END) AS invalid_quantity_rows,
  SUM(CASE WHEN discount_rate < 0 OR discount_rate > 1 THEN 1 ELSE 0 END) AS invalid_discount_rows
FROM retail_sales;
