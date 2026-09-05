import numpy as np

print("== Creating Arrays == ")
arr = np.array([10,20,30,40,50,60,70])
print(arr)

print("\n=== Indexing & Slicing ===")
print(arr[1])
print(arr[0:2])

print("\n=== Vectorized Operations ===")
print(arr + 10)
print(arr * 2)
print(arr ** 2)

print("\n == NumPy Functions ==")
print(arr.sum())
print(arr.mean())
print(arr.min(), arr.max())

print("\n=== Data Cleaning Examples ===")
data = np.array([10,-20,30,-40,50])
clean = data[data >= 15]
print("Cleaned:", clean)

marks = np.array([80,90,-1,75,-1,60])
marks[marks == -1]=marks[marks != 1].mean() 
print("Filled Missing:",marks)# Average of non negative value

cities = np.array(["mumbai","PUNE","Delhi","MUmbai"])
cities = np.char.strip(cities)
cities = np.char.title(cities)
print(cities)






