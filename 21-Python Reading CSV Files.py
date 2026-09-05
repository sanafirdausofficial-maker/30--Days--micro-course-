import csv

# Read Entire CSV
with open("day21_sales_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Read with DictReader
with open("day21_sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Order_ID"],row["Payment_Type"])

# Total sales
total = 0
with open("day21_sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["Price"])*int(row["Quantity"])
print("Total_Sales:",total)


# Filter by city
mumbai = []
with open("day21_sales_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["City"] =="Mumbai":
            mumbai.append(row)
print(mumbai)



