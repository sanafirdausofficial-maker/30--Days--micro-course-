import pandas as pd
from datetime import datetime

# Read CSV file
df = pd.read_csv("day24_Employee_Data.csv")

# 1. Clean Employee Names and Cities
#df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
#df["City"] = df["City"].str.strip().str.title()

#print(df)

# 2. Remove duplicate rows based on Employee_ID(or entire now)
#df = df.drop_duplicates(subset=['Department'],keep='first')
#print(df)

# 3. Add Experience column

current_year = datetime.now().year
df['Experience'] = current_year - df['Joining_Year'].astype(int)

print(df)

# Display cleaned data
#print(df)

# Save the cleaned data
#df.to_csv("day26_clean_employee_data.csv", index=False)



