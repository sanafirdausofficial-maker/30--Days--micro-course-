# String Indexing

name = "Sana"
print(name)
print(name[0])
print(name[3])
print(name[-4])

# String Slicing

product = "Laptop pro 2024"
print(product[-4:0])

text = "Data Analysis"

#Extracting first 4 characters
print("First 4 letters:", text[0:4])  #Data

#Extracting Characters from Middle
print("Middle slice:",text[4:13]) #Analysis

# #Extract till End
print("Till end:", text[4:]) #Analysis

## Extract from beginning
print("From start:", text[:4]) #Data

# # Extract last 5 characters
print("Last 5 letters:", text[-5:]) #alysis

# Skip Text
print("Skip Text:",text[0:13:3])
print("Reverse:", text[4::-1])