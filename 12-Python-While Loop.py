# Basic While Loop

i=1
while i<=10:
    print(i)
    i+=1


# 2 Countdown

n=10
while n>=0:
    print(n)
    n-=1

# 3 Ask User until Valid input
#num = ""
#while not num.isnumeric():
    #num =input("Enter any value:")
    #print("please Enter only number")

#print("Number accepted",num)

# # 4 Loops through List using While

items = ["Apple","Banana","Grapes","Orange"]
i = 0
while i < len(items):
    print(items[i])
    i += 1

# 5 Using Break
x = 1
while x <= 10:
    if x == 5:
        break
    print(x)
    x += 1

# # 6 Using continue
y = 0
while y < 10:
    y += 1
    if y % 2 == 1:
        continue
    print(y)

# 7 password System (Advanced)
password =""
attempts = 0

#while password != "ankush beniwal" and attempts < 3:
    #password = input("Enter Password:")
    #attempts += 1

    #if password == "ankush beniwal":
        #print("Login Successful")
    #else:
        ##if attempts == 3:
        #print("3 attempts expired")

password = input("Enter password:")
    
if password == "Ankush Beniwal":
    print("Login Successful")
else:
        print("Account Locked")

