# Retail Sales Analysis (Practice Project)

## Purpose
A beginner-friendly Data Analyst portfolio project demonstrating data validation, cleaning, exploratory analysis, SQL aggregation, and chart-based reporting.

**Important:** `data/retail_sales_sample.csv` is a synthetic practice dataset generated for this project. Do not describe it as real company/customer data.

## Tech stack
- Python
- pandas
- matplotlib
- SQLite / SQL
- CSV data

## Run locally
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python analysis.py
   ```
5. See the generated CSV summaries and PNG charts in `outputs/`.

## Analysis performed
- Data types and missing-value checks
- Duplicate order ID check
- Invalid quantity, price, discount, and revenue checks
- Monthly revenue trend
- Revenue by category, region, and sales channel
- Top products by revenue
- SQLite table creation and example SQL analysis

## SQL
Open `sql/analysis_queries.sql` for the equivalent queries. The Python script also creates `outputs/retail_sales.db`.

## Before putting this on your resume
Run the project yourself, inspect the outputs, understand each transformation, and write 2–3 findings based on the actual generated results. Since this dataset is synthetic, label it as a practice/personal project. Do not claim business impact or real-world company experience.
