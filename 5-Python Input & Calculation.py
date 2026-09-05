# Input & Typecasting


#name = ("Enter your name:")
#print("Welcome", name)

age=int(input("Enter your age:"))
print(type(age))
age=age+5
print("Your age is:", age)

temperature = float(input("Enter todays's temp: "))
print(type(temperature))

# Convert Number to String
sales = 50000
text = "Total sales:" + str(sales)
print(text)

# Total sales calculator
product = input("Enter product name:")
quantity = int(input("Enter quantity sold:"))
price_per_unit= float(input("Enter price per unit:"))

total_sales = quantity * price_per_unit

print("--------------------------------------")
print("product name:", product)
print("Total sales Amount:", total_sales)

fnum =int(input("Enter first num:"))
snum =int(input("Enter second num:"))

sum= fnum + snum
print(sum)

# Salary Slip calculator
Employee_name = input("Enter employee name:")
Basic_Salary = int(input("Enter Basic salary:"))
Bonus_Amt = int(input("Enter Bonus Amount:"))
Tax_Percentage = float(input("Enter Tax percentage:"))

Gross_Salary = Basic_Salary + Bonus_Amt
Tax_Amount = (Gross_Salary * Tax_Percentage)/100
Net_Salary = Gross_Salary - Tax_Amount


print("\n--------Salary Slip------------")
print("Gross Salary:", Gross_Salary)
print("Tax Amount:", Tax_Amount )
print("Net Salary:", Net_Salary)

# Discount price calculator

item = input("Enter item name:")
Price = float(input("Enter Original Price:"))
Discount = float(input("Discount Percentage:"))

Discount_amount = Price * Discount/100
Final_price = Price - Discount_amount

print("------------------------------------")
print("Final Price of", item, "=", Final_price)

# Student Marks calculator
Student = input("Enter student name:")
Marks_Obtained = float(input("Enter Marks Obtained:"))
total_marks = float(input( "Total Marks:"))

percentage = (Marks_Obtained/total_marks)*100

print("------------------------------------------")
print(Student,"scored",percentage,"%")
