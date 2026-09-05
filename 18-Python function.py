# DAY-18 FUNCTIONS(def,return)



def greet():
    print("Hello Python Learners")
    print("Learning Functions")

greet()

def Welcome(name):
    print("Welcome",name)


Welcome("Sana")

def add(a,b):
    print("a + b :", a+b)
    print("a * b: ", a*b)

add(10,30)

def add(a,b):
    return a + b

def multiple (X):
    return X*2

result = multiple(add(10,30))

print(result)


def clean_text(value):
    return value.strip().title()

output = clean_text("    MUMbai   ")
print(output)

def fix_City(city):
    city = city.lower().strip()
    city = city.replace("mombai","Mumbai")
    city = city.replace("Kolkatta","Kolkata")
    return city.title()
print (fix_City("mombai"))


def get_year(code):
    return code[-4:]

print(get_year("Laptop-2024"))

def is_valid_email(email):
    return "@" in email and "." in email

print(is_valid_email("test@gmail.com"))

def total_salary(Basic, Bonus):
    return Basic + Bonus

print(total_salary(20000,5000))

def stats(nums):
    return min(nums),max(nums), sum(nums),len(nums)


print(stats([10,20,30]))


def clean_list(values) :
    Cleaned = []
    for v in values:
        Cleaned.append(v.strip().title())
    return Cleaned

print(clean_list(["  MUMbai  ","  DELhi  ","  PUne  "]))

