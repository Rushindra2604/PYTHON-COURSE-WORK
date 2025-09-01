class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print("Book Details".center(50,'*'))
        print(f"Book Title: {self.title}\nBook Author: {self.author}\nBook Price: ${self.price}\n")

b1=Book("xyz","tarak",50)

b1.display()

#
class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_annual_Salary(self):
        print(f"Annual Salary of {self.name} is {self.base_salary*12}")

tarak=Employee("Tarak",23456)

tarak.calculate_annual_Salary()

#
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def result(self):
        self.avg= sum(self.marks)/len(self.marks)
        if self.avg<35:
            print(f"{self.name}'s report :\n Average: {self.avg}\nExam Status:Fail")
        else:
            print(f"{self.name}'s report :\n Average: {self.avg}\nExam Status:Pass")

rushi=Student("Rushi",[78,45,90])
sidarth=Student("Sidarth",[56,73,45])
sanjay=Student("Sanajay",[36,32,24])

rushi.result()
sidarth.result()
sanjay.result()

#
class BankAccount:
    def __init__(self,name,balance):
        self.balance=balance
        self.name=name

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f'Dear {self.name},\n{amount} is withdraw')
        else:
            print(f'Dear {self.name},Insufficient Balance')

    def displayBalance(self):
        print(f"\n{self.name} your current balance is {self.balance}")

tarak=BankAccount("tarak",3000)

tarak.displayBalance()
tarak.deposit(23000)
tarak.withdraw(12000)
tarak.displayBalance()

#
class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        self.odometer = 0
        
    def drive(self,km):
        self.odometer+=km

    def show_odometer(self):
        print(f"Odometer: {self.odometer}km \n.")

car1=Car("Suzuki","Baleno")

car1.drive(45000)
car1.show_odometer()

#
class Movie:
    def __init__(self,name,genre,rating):
        self.genre=genre
        self.rating=rating
        self.name=name

    def suitable_for_kids(self):
        if self.rating >18:
            print(f"{self.name} is not suitable_for_kids")
        else:
            print(f"{self.name} is Suitable for kids")

m1=Movie("Rajasaab","Horror",15)

m1.suitable_for_kids()

#
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self,percent):
        self.price = self.price * (percent/100)

    def show_price(self):
        print(f"Discounted Price:{self.price}")

cart=Product("SmartPhone",100000)

cart.discount(15)
cart.show_price()
         
#
class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5)+32

    def to_celsius(self,fahrenheit):
        return (fahrenheit - 32)* 5/9

temp=Temperature(27)

print(temp.to_fahrenheit())
print(temp.to_celsius(105))

#
class InventoryItem:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity

    def update_quantity(self,amount):
        self.quantity += amount

    def display(self):
        print(f"{self.name}: {self.quantity} is in stock")

item=InventoryItem("Rice",100)

item.update_quantity(-50)
item.display()

#
class Order:
    def __init__(self,order_id,status='pending'):
        self.order_id=order_id
        self.status=status

    def update_status(self,new_status):
        self.status=new_status

    def show_status(self):
        print(f"Your Order with {self.order_id} Status:{self.status}")

o1=Order("ORD123","shipped")

o1.show_status()

#
