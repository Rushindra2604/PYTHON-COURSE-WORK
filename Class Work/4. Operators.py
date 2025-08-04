#1. Arthimetic operators
a=29
b=17
print("Addition(+):",a+b) #Addition(+): 46
print("Subtraction(-):",a-b) #Subtraction(-): 12
print("Mul(*):",a*b) #Mul(*): 493
print("Divison(/):",a/b) #Divison(/): 1.7058823529411764
print("Floor Division(//):",a//b) #Floor Division(//): 1
print("Modulus(%):",a%b) #Modulus(%): 12
print("Exponentiation(**):",a**b) #Exponentiation(**): 7257147736730073114838109

#2. Comparision operators
c=26
d=27
print("Equals to(==):",c==d) #Equals to(==): False
print("Not Equals to(!=):",c!=d) #Not Equals to(!=): True
print("Greater than(>):",c>d) #Greater than(>): False
print("Less than(<):",c<d) #Less than(<): True
print("Greater than Equal to(>=):",c>=d) #Greater than Equal to(>=): False
print("Less than Equal to(<=):",c<=d) #Less than Equal to(<=): True

#3. Assignment operators
'''var=var(op)(val)
e=e+10
var(op)=val
e+=10'''
e=36
e+=18
print("Add & Assign(+=):",e) #Add & Assign(+=): 54
e-=18
print("Subtract & Assign(-=):",e) #Subtract & Assign(-=): 36
e*=18
print("Multiply & Assign(*=):",e) #Multiply & Assign(*=): 648
e**=18
print("Exponentiate & Assign(**=):",e) #Exponentiate & Assign(**=): 405835567183366870146612074861360144577666685599744
e/=18
print("Divide & Assign(/=):",e) #Divide & Assign(/=): 2.2546420399075937e+49
e//=18
print("Floor divide & Assign(//=):",e) #Floor divide & Assign(//=): 1.2525789110597743e+48
e%=2
print("Modulus & Assign(%=):",e) #Modulus & Assign(%=): 0.0

#4. Logical Operators
'''
=====AND=====

T AND T = T
T AND F = F
F AND T = F
F AND F = F

(T AND T AND T AND T) = T
(T AND T AND T AND F) = F

=====OR=====

T OR T = T
T OR F = T
F OR T = T
F OR F = F

(T OR T OR T OR T) = T
(T OR F OR T OR T) = T
(F OR F OR F OR T) = T
(F OR F OR F OR F) = F

=====NOT=====

NOT T = F
NOT F = T '''

a =30
b =10
print("and:",a%10==0 and b%10==0) #and: True
print("or:",a%6==0 or b%6==0) #or: True
print("not:",not a%5==0) #not: False

#5. Membership operators
names=['reddy','arjun','charan','surya','tarak','prabhas']
print('in result:','arjun' in names) #in result: True
print('not in result:','akhil' not in names) #not in result: True

#6. Identity Operators
l=[1,2,3,4]
b=[1,2,3,4]
print("l is b:",l==b) #l is b: True
a=b #assigning b to a
print("a is b:",a is b) #a is b: True
print("id(l)",id(l)) #id(l) 1668381455872
print("id(b)",id(b)) #id(b) 1668381298240
print("id(a)",id(a)) #id(a) 1668381298240
print("a is not b:",a is not b) #a is not b: False
print("l is not b:",l is not b) #l is not b: True

#7. Bitwise Operators (With Binary Representation)
'''1-001
2-010
3-011
4-100
5-101
6-110
7-111

3-011
5-101
------
3&5=001=1'''
print("3&5: ",3&5) #3&5:  1

'''4-100
5-101
------
4|5=101=5'''
print("4|5: ",4|5) #4|5:  5

'''5-101
6-110
-------
5^6=011=3'''
print("5^6: ",5^6) #5^6:  3

'''1-001
--------
~1=110'''
print("~1: ",~1) #~1:  -2

'''2<<1
2=010
4=100'''
print("2<<1: ",2<<1) #2<<1:  4

'''4>>1
4=100
2=010'''
print("4>>1: ",4>>1) #4>>2:  8