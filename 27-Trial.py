import pandas as pd
import numpy as np

# -----------------------------
# 1. Load Raw Data
# -----------------------------
df = pd.read_csv("raw_sales_data.csv")

# -----------------------------
# 2. Clean Text Columns
# -----------------------------
text_cols = ["Customer_Name", "City", "State"]

for col in text_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.strip()
        .str.title()
    )

# -----------------------------
# 3. Remove Duplicate Orders
# -----------------------------
df = df.drop_duplicates(subset="Order_ID")

# -----------------------------
# 4. Convert Numeric Columns
# -----------------------------
numeric_cols = ["Quantity", "Unit_Price", "Discount"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

# -----------------------------
# 5. Calculate Total Sales
# -----------------------------
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]

# -----------------------------
# 6. Categorize Order Value
# -----------------------------
conditions = [
    df["Total_Sales"] >= 10000,
    (df["Total_Sales"] >= 5000) & (df["Total_Sales"] < 10000),
    df["Total_Sales"] < 5000
]

choices = ["High", "Medium", "Low"]

df["Order_Value_Category"] = np.select(
    conditions,
    choices,
    default="Low"
)


# -----------------------------
# 7. Summary Reports
# -----------------------------

# Total Sales by City
city_summary = (
    df.groupby("City", as_index=False)["Total_Sales"]
      .sum()
      .sort_values(by="Total_Sales", ascending=False)
)

# Total Sales by Product Category
category_summary = (
    df.groupby("Product_Category", as_index=False)["Total_Sales"]
      .sum()
      .sort_values(by="Total_Sales", ascending=False)
)

# -----------------------------
# 8. Export Outputs to CSV
# -----------------------------
df.to_csv("cleaned_sales_data.csv", index=False)
city_summary.to_csv("total_sales_by_city.csv", index=False)
category_summary.to_csv("total_sales_by_category.csv", index=False)

print("✅ Data processing completed successfully!")
