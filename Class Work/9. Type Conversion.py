#Converting from int
a = 5
print(a,type(a))
# int to Float
f = float(a)
print(f,type(f))
# int to String
s = str(a)
print(s,type(s))
# int to Boolean
b = bool(a)
print(b,type(b))
'''
# int to list
l = list(a)
print(l,type(l)) #TypeError: 'int' object is not iterable
# int to tuple
t = tuple(a)
print(t,type(t)) #TypeError: 'int' object is not iterable
#int to dictionary
d = dict(a)
print(d,type(d)) #TypeError: 'int' object is not iterable
#int to set
set = set(a)
print(s,type(set)) #TypeError: 'int' object is not iterable
'''
#Output:
'''
5 <class 'int'>
5.0 <class 'float'>
5 <class 'str'>
True <class 'bool'> 
'''
# Converting from float
f = 3.4
print(f,type(f))
# float to int
print(int(f), type(int(f)))
# float to string
print(str(f), type(str(f)))
# float to boolean
print(bool(f), type(bool(f)))
'''
# float to list
l = list(f)
print(l,type(l)) #TypeError: 'float' object is not iterable
# float to tuple
t = tuple(f)
print(t,type(t)) #TypeError: 'float' object is not iterable
# float to dictionary
d = dict(f)
print(d,type(d)) #TypeError: 'float' object is not iterable
# float to set
set = set(f)
print(s,type(set)) #TypeError: 'float' object is not iterable
'''

#Output:
'''
3.4 <class 'float'>
3 <class 'int'>
3.4 <class 'str'>
True <class 'bool'> 
'''

#Converting from str
s = 'Rushi'
print(s, type(s))
# string to boolean
print(bool(s), type(bool(s)))
# string to list
print(list(s), type(list(s)))
# string to tuple
print(tuple(s), type(tuple(s)))
# string to set
print(set(s),type(set(s)))
'''
#string to int 
print(int(s), type(int(s))) #ValueError: invalid literal for int() with base 10: 'mani'
#string to float
print(float(s), type(float(s))) #ValueError: could not convert string to float: 'mani'
#string to dictionary
print(dict(s),type(dict(s))) #ValueError: dictionary update sequence element #0 has length 1; 2 is required
'''
#Output:
'''
Rushi <class 'str'>
True <class 'bool'>
['R', 'u', 's', 'h', 'i'] <class 'list'>
('R', 'u', 's', 'h', 'i') <class 'tuple'>
{'h', 'i', 'R', 'u', 's'} <class 'set'> 
'''
# Converting from list
l = [1,2,3,4,5]
print(l, type(l))
# list to string 
print(str(l),type(str(l)))
# list to boolean
print(bool(l), type(bool(l)))
# list to tuple
print(tuple(l), type(tuple(l)))
# list to set
print(set(l),type(set(l)))
'''
# list to int
print(int(l), type(int(l))) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# list to float
print(float(l),type(float(l)))#TypeError: float() argument must be a string or a real number, not 'list'
# list to dictionary
print(dict(l),type(dict(l)))#TypeError: cannot convert dictionary update sequence element #0 to a sequence
'''
#Output:
'''
[1, 2, 3, 4, 5] <class 'list'>
[1, 2, 3, 4, 5] <class 'str'>
True <class 'bool'>
(1, 2, 3, 4, 5) <class 'tuple'>
{1, 2, 3, 4, 5} <class 'set'> 
'''

#Converting from tuple
t = (1,2,3,4,5)
print(t, type(t))
# tuple to string 
print(str(t),type(str(t)))
# tuple to boolean
print(bool(t), type(bool(t)))
# tuple to list
print(list(t), type(list(l)))
# tuple to set
print(set(t),type(set(t)))
'''
# tuple to int
print(int(t), type(int(t))) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
# tuple to float
print(float(t),type(float(t)))#TypeError: float() argument must be a string or a real number, not 'tuple'
# tuple to dictionary
print(dict(t),type(dict(t)))#TypeError: cannot convert dictionary update sequence element #0 to a sequence
'''
#Output:
'''
(1, 2, 3, 4, 5) <class 'tuple'>
(1, 2, 3, 4, 5) <class 'str'>
True <class 'bool'>
[1, 2, 3, 4, 5] <class 'list'>
{1, 2, 3, 4, 5} <class 'set'> 
'''

# Converting from set
s1 = {1,2,3,4,5}
print(s1, type(s1))
# set to string 
print(str(s1),type(str(s1)))
# set to boolean
print(bool(s1), type(bool(s1)))
# set to list
print(list(s1), type(list(s1)))
# set to tuple
print(tuple(s1),type(tuple(s1)))
'''
# set to int
print(int(s1), type(int(s1))) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
# set to float
print(float(s1),type(float(s1)))#TypeError: float() argument must be a string or a real number, not 'set'
# set to dictionary
print(dict(s1),type(dict(s1)))#TypeError: cannot convert dictionary update sequence element #0 to a sequence
'''
#Output:
'''
{1, 2, 3, 4, 5} <class 'set'>
{1, 2, 3, 4, 5} <class 'str'>
True <class 'bool'>
[1, 2, 3, 4, 5] <class 'list'>
(1, 2, 3, 4, 5) <class 'tuple'> 
'''

#Converting from dictionary
d = {1:'Rushi',2:'Arjun',3:'Soorya',4:'Simmba',5:'Anirudh'}
print(d, type(d))
# dictionary to string 
print(str(d),type(str(d)))
# dictionary to boolean
print(bool(d), type(bool(d)))
# dictionary to list
print(list(d), type(list(s1)))#only gets Keys only
# dictionary to tuple
print(tuple(d),type(tuple(d)))#only gets Keys only
# dictionary to set
print(set(d),type(set(d)))#only gets Keys only

'''
# dictionary to int
print(int(s1), type(int(s1))) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
# dictionary to float
print(float(s1),type(float(s1)))#TypeError: float() argument must be a string or a real number, not 'dict'

'''
#Output:
'''
{1: 'Rushi', 2: 'Arjun', 3: 'Soorya', 4: 'Simmba', 5: 'Anirudh'} <class 'dict'>
{1: 'Rushi', 2: 'Arjun', 3: 'Soorya', 4: 'Simmba', 5: 'Anirudh'} <class 'str'>
True <class 'bool'>
[1, 2, 3, 4, 5] <class 'list'>
(1, 2, 3, 4, 5) <class 'tuple'>
{1, 2, 3, 4, 5} <class 'set'> 
'''

# To convert a list to a dictionary, it must be a list of key-value tuples.
d = [('name', 'Rushi'), ('batch', '22'), ('subject', 'python')]
dict(d)
#Output: {'name': 'Rushi', 'batch': '22', 'subject': 'python'}

#Converting from boolean
b = True
print(b,type(b))
# boolean to float
print(float(b),type(float(b)))
# boolean to string

print(str(b),type(str(b)))
# boolean to int
print(int(b),int(int(b)))
'''
# boolean to list
print(list(b),type(list(b))) #TypeError: 'bool' object is not iterable
# boolean to tuple
print(tuple(b),type(tuple(b))) #TypeError: 'bool' object is not iterable
# boolean to dictionary 
print(dict(b),type(dict(b))) #TypeError: 'bool' object is not iterable
# boolean to set
print(set(b),type(set(b))) #TypeError: 'bool' object is not iterable

'''
#Output:
'''
True <class 'bool'>
1.0 <class 'float'>
True <class 'str'>
1 <class 'int'>
'''
