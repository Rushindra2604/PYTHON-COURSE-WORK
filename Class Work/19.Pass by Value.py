#int
def update(n):
    print("Before- Inside of the function:",n)
    n=n+10
    print("After- Inside of the function:",n)

n=10
update(n)
print("outside of the function:",n)

#float
def update(n):
    print("Before- Inside of the function:",n)
    n=n+10
    print("After- Inside of the function:",n)

n=10.8
update(n)
print("outside of the function:",n)

#String
def update(n):
    print("Before- Inside of the function:",n)
    n.append(4)
    print("After- Inside of the function:",n)

n=['1,2,3']
update(n)
print("outside of the function:",n)

#tuple
def update(n):
    print("Before- Inside of the function:",n)
    n={1,2,3,4}
    print("After- Inside of the function:",n)

n={1,2,3,4,5}
update(n)
print("outside of the function:",n)

#dict
def update(n):
    print("Before- Inside of the function:",n)
    n[6]=36
    print("After- Inside of the function:",n)

n={1:1,2:4,3:9,4:16,5:25}
update(n)
print("outside of the function:",n)

#Boolean
def update(n):
    print("Before- Inside of the function:",n)
    n=False
    print("After- Inside of the function:",n)

n=True
update(n)
print("outside of the function:",n)

# Factorial of numbers
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

n=int(input("Enter the Value: "))
print(factorial(n))

#
def shoot(n):
    if n==1:
        return 1
    shoot(n-1)
    print("Before recursion:",n)
    shoot(n-1)
    print("After recursion:",n)

n= int(input("Enter the Value: "))
shoot(n)

#Sum of Digits
n=input("Enter the num: ")
sum=0
for i in n:
    sum+=int(i)
print(sum)


n=int(input("Enter a Number: "))
def sumofdigits(n):
    if n == 0:
        return 0
    return n % 10 + sumofdigits(n//10)
print(sumofdigits(n))

#Fibbonacci series
n=int(input("Enter a number: "))
a=0
b=1
if n==1:
      print(a)
elif n>=2:
    print(a)
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c

# Sum of numbers
def sumofnum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return n+sumofnum(n-1)

n=int(input("Enter the Value: "))
print(sumofnum(n))
