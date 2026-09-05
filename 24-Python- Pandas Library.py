# DAY-24 - PANDAS COMPLETE PRACTICE FILE

import pandas as pd

# LOAD CSV FILE

df = pd.read_csv("day24_Employee_data.csv")
print("\n---Raw Data---")
print(df.head())

# Print("\n--- output ---")

print("\n--- Bottom 5 Rows ---")
print(df.tail())

# BASIC INFORMATION

print("\nShape:", df.shape)
print("\nColumns:",df.columns)
print(df.info())

# # 3 CLEAN TEXT DATA(VERY IMPORTANT)

# Clean Employee Names
#df["Employee_name"] = df["Employee_Name"].str.strip().str.title()
#print(df.head())

#Clean city Names
#df["City"] = df["City"].str.strip().str.title()
#print(df.head())

#print("\n--- Cleaned Text Column---")
#print(df[["Employee_Name","City","Department"]].head())

# # REMOVE DUPLICATES

print("\nDuplicate Rows:",df.duplicated().sum())
df = df.drop_duplicates()

# # 5 FILTER DATA

# Employees from Mumbai
#df["City"] = df["City"].str.strip().str.title()

mumbai_emp = df[df["City"] == "Mumbai"]
print(mumbai_emp)

### Employees with Salary > 60000
high_salary = df[df["Salary"] > 60000]
print(high_salary.head())

#print(\nEmployees from Mumbai:"mumbai_emp.shape[0]")
print("Employee with Salary > 6000:", high_salary.shape[0])

# 6 SORT DATA

#sort by salary (descending)
#df_sorted_salary = df.sort_values("Salary",ascending = False)
#print(df_sorted_salary.head())

# Sort by joining year
df_sorted_Year = df.sort_values("Joining_Year")
print(df_sorted_Year.head())

# # 7.ADD NEW  COLUMNS

# # Salary Categeory
df["Salary_Categeory"] = df["Salary"].apply(
    lambda x: "High" if x >= 60000 else "Medium" if x >= 50000 else "Low" 

)
print(df.head())

#Experience(Years)
df["Experience"] = 2025 - df["Joining_Year"]
print(df.head())

# # 8 GROUPS BY OPERATORS

# # Average salary by Department
avg_salary_depth = df.groupby("Department")["Salary"].sum()
print(avg_salary_depth)

# Total Salary by City
total_Salary_City = df.groupby("City")["Salary"].sum()
print(total_Salary_City)

# # Employee Count by Department
count_dept = df.groupby("Department")["Employee_ID"].count()
print(count_dept)

# # # 9 EXPORT CLEANED DATA-Sort by Salary(Descending)
df_sorted_Salary = df.sort_values("Salary", ascending=False)
print(df_sorted_Salary.head())

df_sorted_Salary.to_csv("employee__sorted_by_Salary.csv",index=False)





