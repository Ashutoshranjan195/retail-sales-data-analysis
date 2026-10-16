from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "retail_sales_sample.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
initial_rows = len(df)

# Parse and validate fields.
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
numeric_cols = ["quantity", "unit_price", "discount_rate", "revenue"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

quality = {
    "rows_loaded": initial_rows,
    "duplicate_order_ids": int(df["order_id"].duplicated().sum()),
    "missing_cells_before_cleaning": int(df.isna().sum().sum()),
    "invalid_quantity_rows": int((df["quantity"] <= 0).fillna(True).sum()),
    "invalid_unit_price_rows": int((df["unit_price"] < 0).fillna(True).sum()),
    "invalid_discount_rows": int(((df["discount_rate"] < 0) | (df["discount_rate"] > 1)).fillna(True).sum()),
}
pd.DataFrame([quality]).to_csv(OUT / "data_quality_report.csv", index=False)

# Basic cleaning: remove duplicate order IDs and rows with missing required values.
df = df.drop_duplicates(subset=["order_id"])
required = ["order_id", "order_date", "region", "sales_channel", "product",
            "category", "quantity", "unit_price", "discount_rate", "revenue"]
df = df.dropna(subset=required)
df = df[(df["quantity"] > 0) & (df["unit_price"] >= 0) &
        (df["discount_rate"].between(0, 1)) & (df["revenue"] >= 0)]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Export useful summaries.
monthly = df.groupby("month", as_index=False)["revenue"].sum().sort_values("month")
category = df.groupby("category", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
region = df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
channel = df.groupby("sales_channel", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
product = df.groupby("product", as_index=False).agg(
    total_revenue=("revenue", "sum"),
    units_sold=("quantity", "sum"),
    orders=("order_id", "count")
).sort_values("total_revenue", ascending=False)

monthly.to_csv(OUT / "monthly_revenue.csv", index=False)
category.to_csv(OUT / "revenue_by_category.csv", index=False)
region.to_csv(OUT / "revenue_by_region.csv", index=False)
channel.to_csv(OUT / "revenue_by_channel.csv", index=False)
product.to_csv(OUT / "product_performance.csv", index=False)

# Save clean data and SQLite database for SQL practice.
clean_path = OUT / "cleaned_retail_sales.csv"
df.drop(columns=["month"]).to_csv(clean_path, index=False)
with sqlite3.connect(OUT / "retail_sales.db") as conn:
    df.drop(columns=["month"]).to_sql("retail_sales", conn, if_exists="replace", index=False)

# Charts (matplotlib only).
plt.figure(figsize=(10, 5))
plt.plot(monthly["month"], monthly["revenue"], marker="o")
plt.title("Monthly Revenue Trend (Synthetic Practice Data)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue_trend.png", dpi=160)
plt.close()

plt.figure(figsize=(8, 5))
plt.bar(category["category"], category["revenue"])
plt.title("Revenue by Category (Synthetic Practice Data)")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUT / "revenue_by_category.png", dpi=160)
plt.close()

# A small text summary based on the actual run.
total_revenue = df["revenue"].sum()
top_category = category.iloc[0] if not category.empty else None
top_region = region.iloc[0] if not region.empty else None
summary_lines = [
    "RETAIL SALES ANALYSIS — RUN SUMMARY",
    f"Rows loaded: {initial_rows}",
    f"Rows retained after validation: {len(df)}",
    f"Total recorded revenue: {total_revenue:.2f}",
]
if top_category is not None:
    summary_lines.append(f"Highest-revenue category in this sample: {top_category['category']} ({top_category['revenue']:.2f})")
if top_region is not None:
    summary_lines.append(f"Highest-revenue region in this sample: {top_region['region']} ({top_region['revenue']:.2f})")
summary_lines += [
    "",
    "Caution: the dataset is synthetic. Findings are for practice only and do not represent a real business."
]
(OUT / "run_summary.txt").write_text("\n".join(summary_lines), encoding="utf-8")
print("\n".join(summary_lines))
print(f"\nOutputs saved to: {OUT}")
