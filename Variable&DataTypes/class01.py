# In below,name is a variable, means it value can be changed anywhere 
#hum jesa hee koi variable banatay han to wo Ram ma apni aik location ma store hojay ga yani ase samajh loo kay aik box reserve hojay ga ram ma jis kay naam hum na diya hoga aor us box ma hmari data type store hogee
  
name = "Izzan Abbas"
father = "Syed Khizar Abbas"
age = 16
college = "Pgc"
fee = 60,000
feeofpgc = 125,000
if "fee" == "feeofpgc":
    check = False
else:
    check = True


 
testnone = None
college2 = college
#Is Ko Broad Mind sa Dekhna ha kay college2 = college means college ka sara data college ma agya ab hum college2 ko aga further use karwasaktay
print ("My Name Is : ",name)
print ("My Father's Name Is : ",father)
print("My Age Is : ",age)
print("My College Name Is : ",college2)
#naming variables may name short or easily readble for others ho aor koi digit sa start nahi karna kunki digit variable ki dosri taraf bhi hosakta ha , agar variable name ma bhi hoa to Mushkil hojay ga identify karna PC aor interpreter ka lia . isi lia Alphabet sa shoru hota , aor dosri taraf issi lia alphabets strings ma aty taka identify hoska.
# There are Five Basic Data Types In Variables
# 1.Integers 
# 2.Float
# 3.String
# 4.Boolean
# 5.None
print(type(name))
print(type(age))
print(type(fee))
print(type(check))
print(type(testnone))
#Naming Variables are 6 that are already done in 10th class book
#keywords Also covers In 10th class book
no01 = 54
no02 = 42
sum = no01 + no02
print(sum)
# operators 
# 1.Arithematic Operator(+,-,*,/,%,**) ,** means power or raise to 
# 2.Relational Operator (<,>,!,!= etc)
# 3.Assigment Operator (=,+=,-=,%=)
# 4.logical Operator (And,Or,Not) 
value1 = 20
#value = value + 20 ki jagah neecha wala syntax use karsaktay
value1 += 20
print(value1)
#Type Casting means conversion of one data type to another
a = "7"
a = int(7)
print(type(a)) 
#type conversion means automatically converted but only for suitable like
a = 60
b = 0.5
print(a+b)

