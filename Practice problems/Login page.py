email,pwd='xyz@gmail.com','xyz@123'
max_attempt=5
curr_attempt=0

while curr_attempt <= max_attempt:
    e=input("Enter the email: ")
    p=input("Enter the password: ")
    if e==email and p==pwd:
        print("Login successful")
        break  # use to break loop
    else:
        print("Invalid email or pwd.Try again!!")
    curr_attempt+=1
else:  # used to show diff statement after attempts
    print("Max attempts are done.try after some time")