#String Input
str = input("Enter a name: ")
print(str, type(str))
# output: 

#Integer Input
num = int(input("Enter a number: "))
print(num, type(num))
# output: 3 <class 'int'>

#Float Input
f_num = float(input("Enter a float value: "))
print(f_num, type(f_num))
# output: 2.6 <class 'float'>

#Input as List (Space-separated)
lis_ss = input("Enter student names (space-separated): ").split()
print(lis_ss, type(lis_ss))
# output: ['Rushi', 'Tarak', 'Arun', 'Gopal', 'Mohith', 'Sumanth'] <class 'list'>
lis_cs = input("Enter values (comma-separated): ").split(',')
print(lis_cs, type(lis_cs))
# output: ['Rushi', 'Tarak', 'Arun', 'Gopal', 'Mohith', 'Sumanth'] <class 'list'>

#List of Integers
lis_int = list(map(int, input("Enter score of each subject: ").split(',')))
print(lis_int, type(lis_int))
# output: [20, 30, 10, 50, 70, 60] <class 'list'>

#List of Floats
lis_float = list(map(float, input("Enter the price each item: ").split(',')))
print(lis_float, type(lis_float))
# output: [20.5, 30.0, 10.75, 50.25, 70.0, 60.5] <class 'list'>

#Tuple Input
tup_inp = tuple(map(int, input("Enter Product ID: ").split()))
print(tup_inp, type(tup_inp))
# output: (101, 102, 103, 104) <class 'tuple'>

#Set Input
set_inp = set(map(int, input("Enter the Student ID: ").split(',')))
print(set_inp, type(set_inp))
# output: {720, 721, 722, 723} <class 'set'>

#Dictionary Input using eval()
dic_inp = eval(input("Enter student information: "))
print(dic_inp, type(dic_inp))
# output: {'name': 'Rushi', 'age': 21, 'marks': 85} <class 'dict'>

#Multiple Inputs with Unpacking
email, password = input("Enter email and password: ").split()
print(f"Your email:{email} and password:{password}")
# output: Your email:Rushi@gmail.com and password:Rushi@123