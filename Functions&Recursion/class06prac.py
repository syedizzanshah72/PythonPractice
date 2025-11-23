# Practice Question No.01
# def avg(a,b,c):
#     return (a+b+c)/2
# average = avg(10,20,70)
# print(average)
# Practice Question No.02
# myList = ["Izzan",87,"NaqviSb",98]
# def length(list):
#     return len(list)
# result = length(myList)
# print(result)
# Practice Question No.03
# crick = ["Pakistan","India","England","USA"]
# def prin_list(list):
#     for items in list:
#         print(items ,end=" ")
# print(prin_list(crick))
# Practice Question No.03
n = 5
def factorial(i):
  fact = 1
  for item in range(1,n+1):
      fact *= item
      print(fact)
factorial(n)
# Practice Question no.04
usd = 283
def conver(i):
    return usd * i
print("The Rate Of Usd $ To Pakistani Rupee Is : ",conver(4))
# Practice Question No.05
enterInput = int(input("Enter A Number You Want To Check : "))
def check(n):
    if  n%2 == 0:
        print( "Your Number Is even")
    else:
        print("odd")
print(check(enterInput))
# Practice Question For Recurrsion
def natural(n):
    if n == 0:
        return 
    print(n)
    natural(n-1) 
natural(6)
# Practice Question
fruits = ["Banana","Mango"]
def print_list(list,idx = 0):
    if(len(list) == idx):
        return
    print(list[idx])
    print_list(list,idx+1)
    
print(print_list(fruits))