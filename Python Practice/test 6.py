class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}")

Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
Book1.display_info()

class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_annual_salary(self):
        return self.base_salary * 12
    
E1 = Employee("Alice", 3000)
print(f"Annual Salary of {E1.name} , emp.calculate_annual_salary()")

class InventoryItem:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self,amount):
        self.quantity += amount

    def display_item(self):
        print(f"Item: {self.name}, Quantity: {self.quantity}")

item1 = InventoryItem("Laptop", 50)
item1.update_quantity(20)
item1.display_item()

class Account:
    def __init__(self,balance):
        self.balance = balance

    def show_balance(self):
        print(f"Balance : {self.balance}")

class SavingsAccount(Account):
    def __init__(self,balance,add_intrest):
        super().__init__(balance)
        self.intrest_rate = intrest_rate
        
