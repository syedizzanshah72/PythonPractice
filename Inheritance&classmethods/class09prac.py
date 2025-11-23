class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 3.14 * self.radius
c1 = Circle(5)
print(c1.area()) 

class Employe:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    def show_details(self):
        print("name",self.name)
        print("role",self.role)
e1 = Employe("Izzan","CEO",89000)
e1.show_details()