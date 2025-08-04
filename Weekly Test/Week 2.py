# Q1. Income Tax Calculator
salary = float(input())
tax_amount = 0
if salary < 250000:
    print("No Tax")
elif salary >= 250001 and salary <= 500000:
    tax_amount = salary * 5/100
    print(tax_amount)
elif salary >= 500001 and salary <= 1000000:
    tax_amount = salary * 20/100
    print(tax_amount)
elif salary > 1000000:
    tax_amount = salary * 30/100
    print(tax_amount)
#Output: 15000.0

# Q2. Movie Ticket Pricing System
n = int(input())
sum = 0
for i in range(n):
    age = int(input())
    if age < 5:
        pass
    elif age >= 5 and age <= 18:
        sum += 100
    elif age >= 19 and age <= 60:
        sum += 150
    elif age == 60:
        sum += 120
print(sum)
#Output: 300

# Q3.Electricity Bill Generator
units = int(input())
bill = 0
if units < 100:
    bill += units * 1.5
    print(bill)
elif units > 100 and units <= 200:
    bill += 150+(units-100) * 2.5
    print(bill)
elif units > 200 and units <= 500:
    bill += 400+(units-200) * 4
    print(bill)
elif units > 500:
    bill += 1600+(units-500) * 6
    print(bill)

# Q4. Car Parking Fee Calculator
hours = int(input())
ex_hours = 0
if hours == 2:
    print(30)
elif hours > 2 and hours < 24:
    ex_hours = hours - 2
    print(30 + ex_hours * 10)
elif hours == 24:
    print(200)
#Output: 40

# Q5. Product Inventory Checker
p_name = input
quantity = int(input())
if quantity == 0:
    print(f"{p_name}: Out of Stock")
elif quantity > 0 and quantity <= 10:
    print(f"{p_name}: Low Stock")
elif quantity > 10 and quantity <= 50:
    print(f"{p_name}: In Stock")
elif quantity > 50:
    print(f"{p_name}: OverStock")

# Q6. Pattern - Row-wise Alternating 0 and 1
n = int(input())
for row in range(n):
    for col in range(n):
        if (row+col) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()
# Output:
'''
0 1 0 1 
1 0 1 0 
0 1 0 1 
1 0 1 0 
'''

# Q7. Gym Subscription Billing
amount = 0
while True:
    print('''1. Monthly-₹500
             2. Quarterly-₹1300
             3. Yearly-₹5000''')
    choice = int(input())
    no_people = int(input())
    if choice == 1:
        amount = no_people * 500
        print(amount)
    elif choice == 2:
        amount = no_people * 1300
        print(amount)
    elif choice == 3:
        amount == no_people * 5000
        print(amount)
    elif choice > 3:
        break
    
# Q8. Billing Bot
amount = float(input())
dis_amount = 0
if amount < 1000:
    print(amount)
elif amount >= 1000 and amount <= 4999:
    dis_amount = amount * 5/100
    print(amount-dis_amount)
elif amount >= 5000 and amount <= 9999:
    dis_amount = amount * 10/100
    print(amount-dis_amount)
elif amount > 10000:
    dis_amount = amount * 15/100
    print(amount-dis_amount)

# Q9. ATM PIN Verification with Blocking Logic
stored_pin = 1234
max_att = 3
for _ in range(3):
    pin = int(input())
    if pin == stored_pin:
        print("Access Granted")
        break
else:
    print("ATM Blocked. Try Again Later.")

#Q10. Bus Booking System- Track full and Empty Seats
total_seats = int(input())
booked_seats = list(map(int, input().split()))
print(f"Total Seats: {total_seats}")
print(f"Booked Seats: {len(booked_seats)}")
print(f"Available: {total_seats - len(booked_seats)}")
#Output:
'''
Total Seats: 4
Booked Seats: 1
Available: 3
'''