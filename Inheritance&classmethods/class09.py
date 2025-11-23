# delete an object or an property is also possible
class Student:
    def __init__(self,name):
        self.name = name
        print(name)
c1 = Student("Izzan")
c2 = Student("Hassan")
# del c1
# print(c1)
# There Are Generally Two type oop
# public And Private
# Private Attributes And Methods
# These Attributes Are Those Which Is not Accessible Outside Class
# if before The name Of variable__ this written it means that is private and not accessible outside class
class Account_No:
    def __init__(self,account_no,accountpassword):
        self.account = account_no
        self.__accountpass = accountpassword # It Becomes Private
    # But It Can Accesible As These
    def resetpass(self):
        print(self.__accountpass)
ac01 = Account_No("657848","ixhdhhh")
print(ac01.resetpass())
# Previous Example Ka Mutabiq Aik private Attribute Ko function may lakar istemal kia jaskta lakin methods ko bahar isi tareeqay sa use kia ja sakta , us metohd ko internally kisi function ma use kia jaskta
class Person:
    __name = "Izzan"
    def __hello(self):
        print("Hello How Are You !")
    def wlcome(self):
        self.__hello()
p1 = Person()
p1.wlcome()
# Inheritance 
# When One Class Derives The properties And Methods From Another class Is Called Inheritance
class Car:
    @staticmethod
    def start():
        print("Car Started ..")
    
    @staticmethod
    def stop():
        print("Car Stop")
class Toyotacar(Car):
    def __init__ (self,name):
        self.name = name
c1 = Toyotacar("Prius")
c2 = Toyotacar("BMW")
print(c1.stop())# It Gives No Error As Thought Beacause It Is Inheritance

# 1. Single Level Inheritance
# 2. Multi-Level Inheritance
# 3. Multi inheritance
# Single level Inheritance Ki Maseel Upar Wale Ha
# Multi level Inheritance ma koi aik Class Dosrii Ki Aor koi Aik In pechli Dono Ki Properties lay ga
class Bat:
    @staticmethod
    def pricestart():
        print("50,000")
    @staticmethod
    def priceend():
        print("40,000,000,000")
class Company(Bat):
    def __init__(self,brand):
        self.brand = brand
class Properties(Company):
    def __init__(self,length):
        self.length = length
b1 = Properties("7cm")
print(b1.priceend())
# Multiple Inheritance
# It means That A derived Class Contains Many Base Class

class A:
    varA = "Welcome To Class A"
class B:
    varB = "Welcome To Class B"
class C(A,B):
    VarC = "Welcome To Class C"
c1 = C()
print(c1.VarC)
print(c1.varB)
print(c1.varA)

# Super Method
# Super Method Is Used To Access Methods Of Parent Methods
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car Has Started")
    @staticmethod
    def  stop():
        print("car has stopped")
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
c1 = ToyotaCar("BMW","Diesel")
print(c1.name)
print(c1.type)   
# Class Method
class Person:
    name = " Miandad"
    def changename(self,name):
        self.name = name
p1 = Person()
p1.changename("Izzan")
print(p1.name)
print(Person.name) 
# There Is An Problem In upper code ka class attribute nahi change oa bas object attribute hee change hoa is problem ko fix karnay ka tareeqay bhot han like
class Person:
    name = " Miandad"
    def changename(self,name):
        Person.name = name # self.__class__.name = name # Iska Matlab bhi Yahi ha
        @classmethod
        def changeName(cls,name):
         cls.name = name
p1 = Person()
p1.changename("Izzan")
print(p1.name)
print(Person.name) 


# Class Methods

@classmethod
def changeName(cls,name):
    cls.name = name # ya Direct Dono jaga pa Change Kardey gi

# Property's Example Is below
class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math
        
    @property
    def percentage(self):
         return str((self.phy + self.che + self.math) / 3 ) + "%"
stu1 = Student(76,98,98)
print(stu1.percentage)  

stu1.phy = 87
print (stu1.percentage)

# Polymorphyism
# when one thing can be used in many differnt situations
class number():
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show(self):
        print(self.real, " i + ", self.img, "j")
    
    def __add__(self, num2):
        real = self.real + num2.real
        img = self.img + num2.img
        return number(real, img)

n1 = number(5, 7)
n1.show()   
num2 = number(6, 7)
num2.show() 
n3 = n1 + num2
n3.show()
