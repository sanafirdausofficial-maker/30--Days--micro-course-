# DAY-20 FILE HANDLING(TEXT FILES)



# # 1) Reading Full File
#print(f.read())


#2 Reading line by line
#with open("Sample.txt","r") as f:
    #for line in f:
        #print(line.strip().title())

# # Writing (overwrite)
#with open("notes.txt","w") as f:
    #f.write("Day 20 - File Handling\n")
    #f.write("Learning read & Write.\n")

# # 4 Appending 
#with open("notes.txt","a") as f:
    #f.write("Appending new content.\n")

# Cleaning data in file
cleaned =[]
#for line in f:
        #cleaned.append(line.strip().title())
#with open("clean_output.txt","w") as f:
    #for city in cleaned:
        #f.write(city + "\n")


## 6) Counting lines
count = 0
with open("sample.txt","r") as f:
    for _ in f:
        count += 1
print("Total lines:",count)








