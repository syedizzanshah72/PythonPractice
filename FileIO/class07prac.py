# with open("prac.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# with open("prac.txt","w") as f:
#     data = f.write(new_data)
# word = "Learning"
# with open("prac.txt","r") as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("Yes,Found")
#     else:
#         print("not Found")
# Practice Question
# def check_word():
#     word = "python"
#     data = True
#     line_no = 1
#     with open("prac.txt","r") as f:
#      while data:
#         data = f.readline()
#         if(word in data):
#             print(line_no)
#             return 
#         line_no += 1
#     return -1
# print(check_word())
# Practice Question
count = 0
with open("numbers.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for value in nums:
        if(int(value) %2 == 0):
            count += 1
print(count)
    
    

    
    
    
       
    