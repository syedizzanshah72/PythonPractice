# Practice Question No.01
userInput = input("Write Your First Name : ")
namelen = len(userInput)
print(namelen)

# Practice Question No.02
count_special = "The No One Knows The Power Of $ In This World"
print("The Existance Of $ In Strig is ",count_special.count("$"))

# Conditional Statements 
#  syntax Are if-elif-else 
enter_marks = int(input("Enter Your Marks In Your last Test "))
if (enter_marks >= 90):
 print("YourGrade According To Your Marks",enter_marks," Is A")
elif(enter_marks >= 80 and enter_marks < 90):
  print("You Grade According To Your marks",enter_marks,"is B")
elif(enter_marks >= 70 and enter_marks < 80 ):
 print("Your Grade Accoring To Your Marks Is ",enter_marks,"C")
elif(enter_marks >= 60 and enter_marks < 70 ):
 print("Your Grade Accoring To Your Marks Is ",enter_marks,"d")
elif(enter_marks < 60 ):
 print("You Are Fail According To Your Marks  ",enter_marks)
else:
 print("Make sure That Are You Give Test")

# Nested If
license = int(input("Enter Your Age "))
if(license >= 18):
    if(license > 80):
        print("You Cannot Drive")
    elif(license == 80):
        print("Drive But Not Recommended")
    else:
        print("Yeah! you Drive")
else:
    print("no")  
    
# Practice Question N0.03
takingInput = int(input("Enter A Number : "))
if (takingInput %2== 0):
    print("Yp It Is even") 
elif(takingInput %2!= 0):
    print("It Is  An Odd Number ",takingInput)  

# Practice Question N0.04
no01inp = int(input("Enter First Number : "))
no02inp = int(input("Enter Second Number : "))
no03inp = int(input("Enter Third Number : "))
no04inp = int(input("Enter Fourth Number : "))
if(no01inp == no02inp == no03inp == no04inp):
    print("All Three Values That You Give Are Equal To Each Other")
elif(no01inp == no02inp  ):
     print("The Two Values That You Are Give Are Equal",no01inp,no02inp)
elif(no01inp == no03inp):
     print("The Values That  You Are Given Are Equal To Each Other",no01inp,no03inp)
elif(no01inp == no04inp):
     print("The Values That  You Are Given Are Equal To Each Other",no01inp,no04inp)
elif(no01inp > no02inp and no01inp > no03inp and no01inp > no04inp):
     print("The Value That Is Greatest Is First Value You gave : ",no01inp)
elif(no02inp > no03inp and no02inp > no01inp and no02inp > no04inp):
    print("The Value That Is Greatest Is Second Value You gave : ",no02inp)
elif(no03inp > no02inp and no03inp > no01inp and no03inp > no04inp):
    print("The Value That Is Greatest Is Third Value You gave : ",no03inp)
elif(no04inp > no03inp and no04inp > no02inp and no04inp > no01inp):
    print("The Value That Is Greatest Is Fourth Value You gave : ",no04inp)
else:
    print("Plz gave Valid Number")
    
# Practice Question No.05
multiof7 = int(input("Enter A Number You Want To Check : "))
modulu = multiof7 % 7
if(modulu == 0):
    print("It Is A multiple Of 7")
else:
    print("No Its Not Multiple")