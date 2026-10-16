# Retail Sales Analysis (Practice Project)

## Purpose
A beginner-friendly Data Analyst portfolio project demonstrating data validation, cleaning, exploratory analysis, SQL aggregation, and chart-based reporting.

**Important:** `data/retail_sales_sample.csv` is a synthetic practice dataset generated for this project. Do not describe it as real company/customer data.

## Tech Stack
- Python
- pandas
- matplotlib
- SQLite / SQL
- CSV data

## Run Locally
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the analysis:

   ```bash
   python analysis.py
   ```

5. See the generated CSV summaries and PNG charts in `outputs/`.

## Analysis Performed
- Data types and missing-value checks
- Duplicate order ID check
- Invalid quantity, price, discount, and revenue checks
- Monthly revenue trend
- Revenue by category, region, and sales channel
- Top products by revenue
- SQLite table creation and example SQL analysis

## SQL
Open `sql/analysis_queries.sql` for the equivalent queries. The Python script also creates `outputs/retail_sales.db`.

## Key Results from the Sample Dataset
- **Rows analyzed:** 300
- **Rows retained after validation:** 300
- **Total recorded revenue:** 29,750.02
- **Highest-revenue category:** Home Office
- **Highest-revenue region:** West

These findings are based on synthetic practice data and do not represent a real business.

## Before Putting This on Your Resume
Run the project yourself, inspect the outputs, understand each transformation, and be prepared to explain your findings. Label this as a personal/practice project. Do not claim real-world company experience or business impact.