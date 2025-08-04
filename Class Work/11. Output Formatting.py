#Printing text
print("Hello, World!")
#Printing Multiple Items
name = 'Rushi' 
age = 21
print("Name:", name, "Age:", age)

#Using sep to Change the Separator
print("2025", "10", "07", sep="-")

#Using end to Control Line Endings
print("Good", end=" ")
print("Morning")
#Output: 
'''
Hello, World!
Name: Rushi Age: 21
2025-10-07
Good Morning 
'''

#Printing Special Characters
print('Printing using Special Characters:')

##NewLine(\n):
print('NewLine:')
print("I'm very happy to meet Arjun after long time.\nHe became lawyer and now he is best criminal lawyer")

##Tab(\t):
print('Tab:')
print("Name:\tArjun")
# output:
'''
Printing using Special Characters:
NewLine:
I'm very happy to meet Arjun after long time.
He became lawyer and now he is best criminal lawyer
Tab:
Name:   Arjun
'''

# Using Commas (Simple Print Method)
print('Printing Using Commas:')
name = "Rushi" 
age = 21
score = 95.2
print("Name:", name, "Age:", age, "Score:", score)

#Using Modulo Operator(%Formatting)
print('Printing Using Modulo Operator:')
name = "Simmba" 
age = 22
score = 78.4
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score) )

#Using f-string
print('Printing Using f-string:')
name = "Soorya" 
age = 23
score = 89
print(f"Name: {name} | Age:{age} | Score:{score:.2f}")

#Using str.format() Method
print('Using str.format() Method:')
name = "Daya" 
age = 22
score = 73
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age, score))

# output:
'''
Printing Using Commas:
Name: Rushi Age: 21 Score: 95.2
Printing Using Modulo Operator:
Name: Simmba | Age: 22 | Score: 78.40
Printing Using f-string:
Name: Soorya | Age:23 | Score:89.00
Using str.format() Method:
Name: Daya | Age: 22 | Score: 73.0
'''