# DAY-17 -RANGE & LOOPS

#Print("\n1") Print 1 to 5")
for i in range(4,10):
    print(i)

#Print ("\n2")Even Numbers(0-18)")
for i in range(0,20,2):
    print(i)


# Print("\n3")Countdown from 0 to 1")
for i in range(10,0,-1):
    print(i)

# Print("\n4")Loop through list Using index")
items = ["pen","Book"," Laptop"]
for i in range(len(items)):
    print(i,items[i])

#Print("\n5")Generate Employee IDs")
for i in range(1,6):
    print("EMP-",i)

print("\n 6)Create years Lists")
years = []
for y in range (2015, 2026):
    years.append(y)
print(years)

# Print ("\n7") Clean city names using range")
cities = ["MUMbai","DElhi","pune"]
for i in range(len(cities)):
    cities[i] = cities[i].strip().title()
print(cities)


# Print("\n8")Extract Last 4 digits from IDs")
ids = ["EMP-001122", "EMP-550044","EMP-990011"]
for i in range(len(ids)):
    print(ids[i][-4:])

for i in range(1,11):
    for j in range(1,4):
        print(f"i value : {i} J value : {j}")


