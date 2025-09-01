from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order: Check chef availability, estimate time,")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order: Check Inventory per item , bag and display")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order: Validate prescription, assign ssecure")

class CloudKitchen(Order):
    def process_order(self):
        print("Processing Cloud Kitchen Order: Vaildate stock,Fast-Delivery")

class TiffinOrder(Order):
    def process_order(self):
        print("Processing Tiffin Order: Validate items,Fast-Delivery")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing Pet Supplies Order: Check pet product actegories")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat/Seafood Order: Confirm freshness,assgin chilled")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order: Custom Baking, time-sensitive paacking")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order: Bulk Cooking, team coordination,")

class JuiceOrder(Order):
    def process_order(self):
        print("Proessing Fresh Juice Order: Immediate prep, cold packaging.")

def handle_order(order):
    order.process_order()

orders = [
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchen(),
    TiffinOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder(),
]

for order in orders:
    handle_order(order)
