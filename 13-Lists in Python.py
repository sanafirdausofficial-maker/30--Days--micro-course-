# # DAY 13 - LISTS


#Create lists
fruits =["Apple","Banana","Mango"]
#print(fruits)

#Indexing
#print(fruits[0])
#print(fruits[-1])

# Update list
#fruits[1] = "Orange"
#print(fruits)

#Add items
#fruits.append("Grapes")
#fruits.insert(1,"Papaya")
#print(fruits)

## Remove items
#fruits.remove("Mango")
#fruits.pop(0)
#print(fruits)

## Slicing 
nums = [10,20,30,40,50]
print(nums[:3])
print(nums[-3:])

## Looping 
for f in fruits:
    print("Fruits:",f)

# # Clean City names
raw = ["MUMbai", "DELhi","Pune"]
clean = []
for c in raw:
    clean.append(c.strip().title())
print(clean)

## Replace Wrong spellings
wrong = ["Kolkatta","Bengluru"]
fixed =[]
for c in wrong:
    c = c.replace("Kolkatta","Kolkata").replace("Bengluru","Bengaluru")
    fixed.append(c)
print(fixed)

## Extract Years
codes = ["Laptop-2024","Phone-2023"]
years = []
for c in codes:
    years.append(c[-4:])
print(years)


