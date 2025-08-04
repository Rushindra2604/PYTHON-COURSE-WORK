# This code snippet demonstrates the use of various data types in Python.
# this done with the context of a icici mobile banking.
# integer
account_number: 123456789058
pincode: 1234
print(type(account_number)) # Output: <class 'int'>
print(type(pincode))  # Output: <class 'int'>

#string
customer_name = "Dasari Rushindra Reddy"
bank_name = "Icici Bank"
email = "rushindra@icici.com"
print(type(customer_name))  # Output: <class 'str'>
print(type(bank_name))  # Output: <class 'str'>
print(type(email))  # Output: <class 'str'>

#float
account_balance = 32000.41
interest_rate = 7.8
deposit_amount = 18000.00
print(type(account_balance))  # Output: <class 'float'>
print(type(interest_rate))  # Output: <class 'float'>
print(type(deposit_amount))  # Output: <class 'float'>

#list
transaction_history = ["Deposit: 18000", "Withdraw: 2000", "Transferred: 5000"]
beneficiaries = ["Padamati Venu", "Sai Kishore", "Sai Tendulkar"]
print(type(transaction_history))  # Output: <class 'list'>
print(type(beneficiaries))  # Output: <class 'list'>

#tuple
bank_details = ("ICICI Bank","Savings Account", "10000")
atm_location = ("ICICI ATM", "Vidyanagar", "Karimnagar", "505001")
print(type(bank_details))  # Output: <class 'tuple'>
print(type(atm_location))  # Output: <class 'tuple'>

#set
IFSC_codes = {"ICICI001", "ICICI002", "ICICI003"}
services_availed = {"Net Banking", "Mobile Banking", "SMS Alerts"}
print(type(IFSC_codes))  # Output: <class 'set'>
print(type(services_availed))  # Output: <class 'set'>

#dictionary
customer = {"name": "Rushindra Reddy","account_number": 1234567890,"balance": 25489.75,"email": "rushindra@icici.com","is_active": True}
transaction = {"txn_id": "TXN78945","type": "NEFT","amount": 5000.00,"date": "2025-07-10","status": "Success"}
print(type(customer))  # Output: <class 'dict'>
print(type(transaction))  # Output: <class 'dict'>

# boolean
is_account_active = True
is_eligible_for_loan = False
transaction_success = True
print(type(is_account_active))  # Output: <class 'bool'>
print(type(is_eligible_for_loan))  # Output: <class 'bool'>
print(type(transaction_success))  # Output: <class 'bool'>

#using by comma sep parameter in print function
account_number: 123456789058
customer_name = "DasariRushindra Reddy"
balance = 25489.75
print("Customer Name", customer_name, "Account Number", account_number, "Balance", balance, sep=',')
#output: Customer Name,DasariRushindra Reddy,Account Number,123456789058,Balance,25489.75

# using f-string for formatted output
account_number: 123456789058
customer_name = "DasariRushindra Reddy"
balance = 25489.75
print(f"Hello {customer_name}, your account ({account_number}) at {bank_name} has a balance of ₹{balance:.2f}.")
# Output: Hello DasariRushindra Reddy, your account (123456789058) at Icici Bank has a balance of ₹25489.75.

# using format method for formatted output
account_number: 123456789058
customer_name = "DasariRushindra Reddy"
bank_name = "Icici Bank"
balance = 25489.75
print("Hello {}, your account ({}) at {} has a balance of ₹{:.2f}.".format(customer_name, account_number, bank_name, balance))
# Output: Hello DasariRushindra Reddy, your account (123456789058) at Icici Bank has a balance of ₹25489.75.