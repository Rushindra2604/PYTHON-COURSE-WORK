from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} via PayPal.")

def process_payment(payment, amount):
    payment.make_payment(amount)

process_payment(CreditCardPayment(), 100)
process_payment(PayPalPayment(), 200)
