# DAY-16 -SETS



#Create set
fruits = {"Apple","Banana","Apple","Mango"}
print(fruits)

# Add item
fruits.add("Orange")
print(fruits)

#Remove item
fruits.discard("Banana")
print(fruits)

# Set operations
a = {1,2,3}
b = {3,4,5}

print("union",a | b) 
print("intersection", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Remove Duplicates
cities = ["Mumbai","Pune","Delhi","Mumbai"]
unique = set(cities)
print("unique Cities:", unique)

# # Missing Values
#list1 = {"SQL","Excel","Power BI"}
#list2 = {"SQL","Power BI"}
#missing = list1 - list2
#print("Missing:", missing)

# Common Skills 
deptA = {"SQL","Excel","Python"}
deptB = {"Excel","Python","Power BI"}
print("Common Skills:", deptA & deptB)
