# Practice Question 
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
# Practice Question 
class Bank_Details():
    def __init__(self,balance,accountno):
        self.balance = balance
        self.account = accountno 
        
        
    def debit(self,debitmoney):
        self.balance -= debitmoney
        print("The Amount ",debitmoney,"Is Debited")
        print("Remaining Amount Is",self.current_balance())
        
        
    def deposit(self,depositmoney):
     self.balance += depositmoney
     print("The Amount",depositmoney,"Is Credited")
     print("Remaining Amount Is",self.current_balance())
     
     
    def current_balance(self):
       return self.balance

    
        
bank = Bank_Details(40000,73317628)
bank.debit(1000)
bank.deposit(7000)
bank.deposit(79000)

bank02 = Bank_Details(90000,9879556)
bank02.deposit(8000)
