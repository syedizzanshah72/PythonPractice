# Loops     Loops Means Repatative
# While Loop Or For Loop Are 2 Types
# While Loop Are Use in those cases when we perform some calculations
# for loop are use in those cases when we want to traverse with data like tuple, string
# While Loop
i = 1
while i < 10:
    print("Hello World")
    i+= 1
# Break And Continue KeyWords
#Break when condition is reaches
i = 1
while i <= 10:
    if i == 3:
        break
    print(i)
    i += 1
# continue means skip
i = 1
while i <= 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


# For Loop     ,It Also contains else at the end which is optional 
# Break And Continue Also exists in For Loop
players = ["Babar Azam","Muhammad Rizwan","Shaheen Shah Afridi","Shadab Khan","Naseem Shah"]
for names in players:
    print(names)
mynamecharacters = "M.Izzan Abbas"
for car in mynamecharacters:
    print(car)
else:
    print("I Use In Those cases when you want a loop executes completely")
# Range Function
# Range Function syntax Are 
for i in range(0,9,2):# In This example first and last perameteres are not optional and middle one is compulsory Beacuse in This example first perameter has starting value which have default zero and on last it is step value which is 1 in default and written integer tells the jump and middle or last value of range is compulsory
    print(i)