# DAY 27 – AI GENERATED PANDAS SALES PIPELINE & AUTOMATION

import pandas as pd

print("Sales Pipeline Started...")

# ------------------------------------------------------------
# 1. LOAD RAW SALES DATA
# ------------------------------------------------------------
df = pd.read_csv("raw_sales_data.csv")
print("Rows Loaded:", df.shape[0])

# ------------------------------------------------------------
# 2. CLEAN TEXT COLUMNS
# ------------------------------------------------------------
df["Customer_Name"] = df["Customer_Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["State"] = df["State"].str.strip().str.title()
df["Product_Category"] = df["Product_Category"].str.strip().str.title()
df["Product_Name"] = df["Product_Name"].str.strip().str.title()

# ------------------------------------------------------------
# 3. REMOVE DUPLICATES
# ------------------------------------------------------------
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print("Duplicates Removed:", before - after)

# ------------------------------------------------------------
# 4. FIX DATA TYPES
# ------------------------------------------------------------
df["Quantity"] = df["Quantity"].astype(int)
df["Unit_Price"] = df["Unit_Price"].astype(float)
df["Discount"] = df["Discount"].astype(float)

# ------------------------------------------------------------
# 5. FEATURE ENGINEERING
# ------------------------------------------------------------

# Total Sales
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]

# Order Value Category
df["Order_Category"] = df["Total_Sales"].apply(
    lambda x: "High" if x >= 50000 else "Medium" if x >= 20000 else "Low"
)

# ------------------------------------------------------------
# 6. FILTER IMPORTANT DATA
# ------------------------------------------------------------

high_value_orders = df[df["Order_Category"] == "High"]
online_sales = df[df["Sales_Channel"] == "Online"]

# ------------------------------------------------------------
# 7. GROUP & AGGREGATE
# ------------------------------------------------------------

city_sales = df.groupby("City").agg(
    Total_Revenue=("Total_Sales", "sum"),
    Order_Count=("Order_ID", "count")
).reset_index()

category_sales = df.groupby("Product_Category").agg(
    Total_Revenue=("Total_Sales", "sum"),
    Order_Count=("Order_ID", "count")
).reset_index()

# ------------------------------------------------------------
# 8. SORT RESULTS
# ------------------------------------------------------------
city_sales.sort_values("Total_Revenue", ascending=False, inplace=True)
category_sales.sort_values("Total_Revenue", ascending=False, inplace=True)

# ------------------------------------------------------------
# 9. EXPORT OUTPUT FILES
# ------------------------------------------------------------
df.to_csv("sales_cleaned_data.csv", index=False)
high_value_orders.to_csv("high_value_orders.csv", index=False)
online_sales.to_csv("online_sales.csv", index=False)
city_sales.to_csv("city_sales_summary.csv", index=False)
category_sales.to_csv("category_sales_summary.csv", index=False)

print("Sales Pipeline Completed Successfully.")
print("Files Generated:")
print("- sales_cleaned_data.csv")
print("- high_value_orders.csv")
print("- online_sales.csv")
print("- city_sales_summary.csv")
print("- category_sales_summary.csv")
