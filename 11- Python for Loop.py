# DAY 11 - For Loop



# 1 Basic Loop

for i in range(1,11):
    print(i)

# 2 Print Characters
Word = "Python"

for Alphabet in Word:
    print(Alphabet)

Word2 = "SQL"
for j in range(1,11):
    print(Word2)

# # 3 Loop through list

items = ["pen","Book","Laptop"]
for item in items:
    print(item)

# # 4 Even numbers
print("print Odd numbers:")
for n in range(0,21,2):
    print(n)

# # 5 Total Calculation

marks = [78,82,90]
total = 0
for m in marks:
    total += m
print("Total:",total)

# # 6 Clean city names
cities = ["  MUMbai","pune  ","  CHENNAI"]
cleaned = []
for c in cities:
    cleaned.append(c.strip().title())
print(cleaned)

# 7 Loops With IF condition
nums = [5,12,3,18,7]
for n in nums:
    if n % 2 == 0:
        print(n,"- is even number")
    else:
        print(n, "- is odd number")

# 9 Extract Last Digits from IDs

ids = ["EMP-01122","EMP-889900"]
for last4 in ids:
    print(last4[-5:])

#Looping through Dictionary
student = {"name":"sana","age":20,"City":"Patna"}

for key,Value in student.items():
 print(key,":",Value)





