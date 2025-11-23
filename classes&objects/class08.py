#OOP Stands For Object Oriented Programming
# To Map Real World Scenerios ,This Code Helps
# Classes And Objects In Python
# Classes Are The Blueprints Of Objects

# Constructor , Python Lazmi Constructor ko call Karta ha , chahay kuch bhi  na likha ho
# All Classes Have A Function __init__ (),which Is Always Executed when object is initiated
# Constructor Is __init__() which Always Executed
class Name:
    def __init__(self,fullname,numbers):
        print("Adding Student To The Data Base")
        self.name = fullname
        self.number = numbers
s1 = Name("Izzan",542)
print(s1.name,s1.number)
s2 = Name("daniyal",492)
print(s2.name,s2.number)
# Class And Instance Attributes
# Class Atribute Is same Everywhere And written Before Constructor While Instance Attribut Value Can Be Changed Anywhere And Is written In Self
class Bike_Details:
    def __init__(self,name,model,company):
        self.name = name
        self.model = model
        self.company = company
    def welcome(self):
        return self.name
c1 = Bike_Details("Izzan",2022,"Honda")
print(c1.name,c1.model,c1.company)
c2 = Bike_Details("Khizar Abbas",2007,"Pak Hero")
print(c2.name,c2.model,c2.company)
print(c1.welcome())

# Class Methods Class Contain two things i. methods,ii.attributes
# Methods Are Functions belongs to object
class Student_data:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def avg_marks(self):
        sum = 0
        for item in self.marks:
            sum += item
        print("Hi",self.name,"Your avg Score is ",sum/3 )
    @staticmethod # Decorater
    def hi():
        print("hello")
    
s1 = Student_data("Izzan",[98,97,92])
s1.avg_marks()
s1.hi()
# s1.name = "mizzan"# directly bhi change karsakta
# Static Methods 
# Static Methods Are Use When No Self Is Needed
# There Are Four Pillars Of OOP Are
# 1.Abstraction 2.Encapsulation 3.Inheritance 4.Polymorphyism
# 1.Abstraction
# Hiding The Implementation Details of a class and only showing necessary Feature to the user 
class Car:
    def __init__(self):
        self.acc = False
        self.bre = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True
c1 = Car()
c1.start()