# # DAY -14 TUPLES
fruits = ("Apple","Banana","Mango")
print(fruits)

# Indexing
print(fruits[0])
print(fruits[-1])

# # Slicing
nums = (10,20,30,40,50)
print(nums[3:])

# # Looping
colors = ("Red","Blue","Green","Orange")
for c in colors:
    print(c)

# # Tuple length
print(len(colors))

# # Concatenation
a = (1,2)
b = (3,4)
print(a + b)

# # packing and Unpackaging
data = ("Laptop", 45000,"Black")
Product, price, color = data
print(Product,price,color)
print(f"product:{Product} price : {price} and color : {color}")

# # Nested tuples inside list
employee = [("E101","Rohit", "pune"), ("E102", "Sneha","Mumbai")]
for eid ,name,city in employee:
    print(eid,name,city) 







