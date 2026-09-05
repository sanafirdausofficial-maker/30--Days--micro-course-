# # DAY-15 DICTIONARIES

Student = {"name":"Rohit","age":21,"City":"Pune"}
print(Student)

# # Accessing Values
print(Student["name"])
print(Student["City"])

# # Adding and Updating
Student["marks"] = 85
Student["City"] = "Mumbai"
print(Student)

# Removing
Student.pop("age")
print(Student)

# Dictioary Methods
print(Student.keys())
print(Student.values())
print(Student.items())
print(Student.get("name"))

# Looping
for k in Student:
    print(k,Student[k])

#Nested dictinary
employees = {
    "E101":{"name":"Rohit", "city":"Pune"},
    "E102":{"name":"Sneha", "city":"Delhi"}
}
print(employees["E102"]["name"])


#Mapping Wrong -> Correct
mapper = {
    "mombai":"Mumbai",
    "Kolkatta":"Kolkata"
}

print(mapper["mombai"])