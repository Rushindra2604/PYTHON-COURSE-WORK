#
def add(a,b):
    return a+b

print(f"The sum is: {add(2,3)}")

#
def square(a):
    return a * a

print(f"The Square is: {5 * 5}")

#
def area(r):
    return r

print(f"The area is: {3.14*(3 * 3)}")

#
def greet(name):
    print(f"Hello, {name}")

name = input()
greet(name)

#
def conversion(deg):
    return deg*9/5 + 32

deg = float(input())
print(f"Temperature in Fahrenheit: {conversion(deg)}")

#
def mul(a,b,c):
    return a*b*c

a,b,c=list(map(int,input().split()))
print(mul(a,b,c))

#
def simpleintrest(p,t,r):
    return (p*t*r)/100

p,t,r=tuple(map(int,input().split()))
print(simpleintrest(p,t,r))

#
def length(s):
    l=0
    for i in s:
        l+=1
    return l

s=input()
print(length(s))

#
def double(l):
    for i in range(len(l)):
        l[i]=l[i]*2
    return l

l=list(map(int,input().split()))
print(double(l))

#
def double(l):
    res = 
    for i in range(len(l)):
        l[i]=l[i]*2
    return l

l=list(map(int,input().split()))
print(double(l))

#remove particular 
def remove(l,val):
    while val in l:
        l.remove(val)
    return

l = list(map(int,input().split()))
val = int(input())
print(remove(l,val))

#
