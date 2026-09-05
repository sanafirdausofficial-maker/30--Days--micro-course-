import pandas as pd

# Load Cleaned employee data
df = pd.read_csv("day24_Employee_Data.csv")

print("\n--- Data Loaded ---")
print(df.head())

# # FILTERING
# Employee from mumbai
mumbai_emp =  df[df["City"] == "Mumbai"]
print(mumbai_emp)

# # High Salary employee
high_salary = df[df["Salary"] >60000]
print()

#Multiple Condition
mumbai_emp = df[df["City"] == "Mumbai"]
print(mumbai_emp)

# # High Salary employeee
high_Salary = df[df["Salary"] > 60000]
print(high_Salary)

# Multiple conditions
mumbai_high = df[(df["City"] == "Mumbai") & (df["Salary"]  > 60000)]
print(mumbai_high)

# Using isin()
IT_and_Finance=df[df["Department"].isin(["IT","Finance"])]
print(IT_and_Finance)

# # Advance Sorting

# # Sort by Salary descending
df_sorted_Salary = df.sort_values("Salary",ascending=False)
print(df_sorted_Salary)

# Sort by Department by Salary
df_sorted_multi = df.sort_values(["Department","Salary"],ascending=[True,False])
print(df_sorted_multi)

#GROUP BY OPERATIONS
#Average salary by department 
avg_Salary_dept = df.groupby("City")["Salary"].sum()
print(avg_Salary_dept)

# # Employee count by Department
emp_count_dept = df.groupby("Department")["Employee_ID"].count()
print(emp_count_dept)

# # Multiple aggregation
Salary_Stats = df.groupby("Department")["Salary"].agg(["min","max","mean","count"])
print(Salary_Stats)

print("\nSalary_Stats:")
print("Salary_Stats")

# # SORT GROUPBY RESULT 
sorted_avg_Salary = avg_Salary_dept.sort_values(ascending=False) 
print("\nDepartment by avg_Salary:")
print("sorted_avg_salary")


