# Functions And Recurrsions
# Function Definition
def cal_sum(a,b):# function Parameters
    return a+b
sum = cal_sum(5,7)# calling function:function Arguments , Values of arguments stored in parameters
print(sum)
# Function Which can return nothing or dont take any argument or perimeter exists
# Default Parameters also have , but conditions.
# Recursions
# When A Function Calls Itself Repeatedly
def show(n):
    if n == 0:
        return 
    print(n)
    show(n-1)
show(6)
def fact(n):
    if n == 0 or n == 1 :
        return 1
    return fact(n-1)
print(fact(9))