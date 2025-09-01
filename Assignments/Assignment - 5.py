# -------------------- ENCAPSULATION --------------------
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd   # private variable

    def getpassword(self):
        return self.__pwd

    def setpassword(self, newpassword):
        self.__pwd = newpassword


# -------------------- INHERITANCE --------------------
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def show_balance(self):
        print(f"Account {self.account_number} balance: ₹{self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest of ₹{interest} added. New balance: ₹{self.balance}")


# -------------------- ABSTRACTION --------------------
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def transfer(self, amount):
        pass


class NEFT(Payment):
    def transfer(self, amount):
        print(f"NEFT Transfer of {amount} initiated. Processing time: upto 2 hours")


class RTGS(Payment):
    def transfer(self, amount):
        print(f"RTGS Transfer of {amount} is initiated. Amount 2 Lakhs+ Processing time: Instant")


class IMPS(Payment):
    def transfer(self, amount):
        print(f"IMPS Transfer of {amount} is initiated. Processing time: Instant and 24/7")


# -------------------- POLYMORPHISM --------------------
class BillPayment:
    def __init__(self, amount):
        self.amount = amount


class ElectricityBill(BillPayment):
    def pay_bill(self):
        return f"Electricity bill of ₹{self.amount} paid successfully"


class MobileRecharge(BillPayment):
    def pay_bill(self):
        return f"Mobile recharge of ₹{self.amount} done successfully"


class CreditCardBill(BillPayment):
    def pay_bill(self):
        return f"Credit card bill of ₹{self.amount} paid successfully"


# -------------------- MAIN MENU --------------------
while True:
    print("\n===== OOPS Concepts Menu =====")
    print("1. Encapsulation Example")
    print("2. Inheritance Example")
    print("3. Abstraction Example")
    print("4. Polymorphism Example")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ENCAPSULATION DEMO
    if choice == "1":
        print("\n--- ENCAPSULATION DEMO ---")
        user = User("Rushindra", "Rushi@123")
        print(f"Username: {user.name}")
        print("Old Password:", user.getpassword())
        newpwd = input("Enter new password: ")
        user.setpassword(newpwd)
        print("Updated Password:", user.getpassword())

    # INHERITANCE DEMO
    elif choice == "2":
        print("\n--- INHERITANCE DEMO ---")
        s = SavingsAccount(1234567890, 80000, 5)
        s.show_balance()
        s.add_interest()

    # ABSTRACTION DEMO
    elif choice == "3":
        print("\n--- ABSTRACTION DEMO ---")
        payments = [NEFT(), RTGS(), IMPS()]
        amt = float(input("Enter transfer amount: "))
        for p in payments:
            p.transfer(amt)

    # POLYMORPHISM DEMO
    elif choice == "4":
        print("\n--- POLYMORPHISM DEMO ---")
        while True:
            print("\n---- Bill Payment Menu ----")
            print("1. Pay Electricity Bill")
            print("2. Mobile Recharge")
            print("3. Pay Credit Card Bill")
            print("4. Back to Main Menu")

            sub_choice = input("Enter your choice (1-4): ")

            if sub_choice == "1":
                amt = float(input("Enter Electricity Bill amount: "))
                bill = ElectricityBill(amt)
                print(bill.pay_bill())

            elif sub_choice == "2":
                amt = float(input("Enter Mobile Recharge amount: "))
                bill = MobileRecharge(amt)
                print(bill.pay_bill())

            elif sub_choice == "3":
                amt = float(input("Enter Credit Card Bill amount: "))
                bill = CreditCardBill(amt)
                print(bill.pay_bill())

            elif sub_choice == "4":
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
