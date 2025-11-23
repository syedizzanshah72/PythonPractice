# # Practice Question No.01
# i = 1
# while i <= 100:
#     print(i)
#     i+= 1
# # Practice Question No.02
# i = 100
# while i >= 1:
#     print(i)
#     i-= 1
# # Practice Question No.03
# i = 1
# userInput = int(input("Enter A Table You Want To Print : "))
# while i <= 10:
#     print(userInput ,"X",i,"=",userInput*i)
#     i+= 1
# # Practice Question No.04
# # This is Looking Complex
# nums = [1,4,9,16,45,76,89,111]
# idx = 0 # ya variable sirf nums kay index ko access karnay ka lia banaya
# while idx < len(nums):
#     print(nums[idx])
#     idx+= 1
# Practice Question No.05
numb = (2,5,8,9,6,7)
x = 7
i = 0
while i < len(numb):
    if (numb[i] == x):
        print("Found",i)
    else:
        print("Finding")
    i+= 1
    
# Practice Question Myself
i = 1
while i < 10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i +=  1
# nums = [1,5,7,9,4,7,9,5,4,3]
# for i in nums:
#     print(i)
# find = (2,8,67,87,90,67)
# x = 67
# idx = 0
# for fin in find:
#     if(fin == x):   
#      print("Yeh X Is find At An Index",idx)
#     idx += 1
for i in range(100,0,-1):
    print(i)
userInput = int(input("Enter A Table you Want And From wwhere"))
for table in range(1,11):
    print(userInput * table)
# Practice Question 
userValue = int(input("Enter The Last Value You Want to Sum : "))
valueDecrement = userValue - 1
while userInput > 0:
    print(userValue + valueDecrement )
    while(valueDecrement == 0):
        break
        valueDecrement -= 1
# Practice Question 
n = 5
fact = 1
for i in range(1,n+1):
    fact **= i
print(fact)
    
    
    