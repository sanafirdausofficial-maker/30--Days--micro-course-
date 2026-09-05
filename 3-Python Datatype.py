# Learning DataType in python
# 7 Data Types

#1 Text Datatype
#String
Customer_name ="Rohit"
print("Customer name =", Customer_name)
print("Customer Datatype=", type(Customer_name))

#2 Numeric Datatype
#2.1 Integer complete Number
rating = 4
order_Quantity = 3

print("rating Datatype=", type(rating))
print("Datatype=", type(order_Quantity))

#2.2 Float-Decimal Number
order_amount = 8599.50

print("order_amount Datatype=", type(order_amount))


#2.3 Complex Number
a = 3+4j

print(type(a))

# 3 Bool(True/False)
is_paid = True

print("is_paid Datatype=", type(is_paid))

# 4 Sequence
# 4.1 - List
Cities = ["Mumbai","Delhi","Pune","Chennai"]
print(Cities)

print(type(Cities))

# 4.2- Tuples
Dimensions=(1920,1080)
print(Dimensions)

print(type(Dimensions))

# 4.3 Range
num = range(5)
print(list(num)) #[0,1,2,3,4]

print(type(num))

Days = range(1,31) # 1 to 30 Days
print(list(Days))

# 5 Dictionary(Dict)
student ={
    "Name": "Anvi",
     "age": 20,
     "City": "Mumbai"

}

print(student)
print(type(student))

# 6 Set
numbers = {1,2,2,3,4}
print(numbers) #Output:{1,2,2,3,4}

print(type(numbers))

# 7 NoneType - No Value
remarks = None
print(remarks,type(remarks))