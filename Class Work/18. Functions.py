#Positional Arguments
def greet(gender,name,age):
    print(name,age,gender)

greet('Roy',21,'Male')

#Keyword Arguments
def greet(name,age,gender):
    print(name,age,gender)

greet(name='Roy',age=21,gender='Male')

#Default Arguments
def greet(name,age,gender,status='absent'):
    print(name,age,gender,status)

greet(name='Roy',age=21,gender='Male',status='present')

#Variable length Arguments
def greet(*var):
    print(var)

greet('Roy',21,'Male','present')
greet('Roy','Male')

#Arbitary Keyword Arguments
def greet(**var):
    print(var)

greet(name='Roy',age=21,gender='Male',status='present')
greet(name='Roy',gender='Male')

#
def display(name,pwd,email):
    print(name,email,pwd)


name,email,pwd='rushi','rushi@gmail.com','rushi@123'
display(name,email,pwd)

#
def wish(name):
    print(f'Welcome to Python {name}!!!')

name = input("Enter Your name: ")
wish(name)

#
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

n= int(input("Enter the Number: "))
for i in range(1,n+1):
    print(f"{i}!={factorial(i)}")

#
def sum(n):
    num=0
    for i in range(1,n+1):
        num=num+i
    return num

n= int(input("Enter the Number: "))
print(f"{n}{sum(n)}")