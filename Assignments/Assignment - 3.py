print(f"Welcome to Python Quiz Competiton")
count = 0

print(f"Question 1: Which of the following is not a datatype?")

while True:
    print('''
1.int
2.float
3.yield
4.dict
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '3':
        print("✅Correct!\n")
        count+=1
        break
    else:
        print(f"❌Wrong! the correct answer is '3'.\n")
        break
        
print(f"Question 2: Which keyword is used to define a class in Python?")

while True:
    print('''
1.def
2.class
3.cls
4.object
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        print("✅Correct!\n")
        count+=1
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 3: What does OOP stand for?")

while True:
    print('''
1.Only Object Python
2.Object-Oriented Programming
3.Open-Origin Programming
4.Organized Object Programming
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        print("✅Correct!\n")
        count+=1
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 4: How do you start a single line comment in Python?")

while True:
    print('''
1.//
2.<!--
3./*
4.#
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '4':
        print("✅Correct!\n")
        count+=1
        break
    else:
        print(f"❌Wrong! the correct answer is '4'.\n")
        break

print(f"Question 5: What does elif stand for?")

while True:
    print('''
1.Else If
2.End Loop If
3.Extra Loop If
4.Exit If
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '1':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '1'.\n")
        break

print(f"Question 6: What does the >= operator check?")

while True:
    print('''
1.Less than
2.Greater than or equal to
3.Equal to
4.Not equal to
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 7: Which of these must end with a colon (:)?")

while True:
    print('''
1.print()
2.switch statement
3.else statement
4.Variable assignment
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '3':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '3'.\n")
        break

print(f"Question 8: Is a condition required for an if statement to work?")

while True:
    print('''
1.Yes
2.No
3.Only sometimes
4.Only with strings
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '1':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '1'.\n")
        break

print(f"Question 9: Can a comment span multiple lines using # symbol?")

while True:
    print('''
1.No
2.Yes, but each line must begin with #
3.None
4.Error
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 10: Can tuple() convert an empty list to a tuple?")

while True:
    print('''
1.No
2.Yes
3.Only if it has numbers
4.Only if it has strings
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 11: Which list can be converted to a dictionary using dict()?")

while True:
    print('''
1.[('x', 1)]
2.[1, 2]
3.['a', 'b', 'c']
4.[1]
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '1':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '1'.\n")
        break

print(f"Question 12: What does 4 > 3 > 2 return?")

while True:
    print('''
1.True
2.False
3.None
4.Error
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '1':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '1'.\n")
        break

print(f"Question 13: Which protocol is often used in ATM software to communicate with the bank’s server?")

while True:
    print('''
1.HTTP
2.FTP
3.SMTP
4.ISO 8583
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '4':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '4'.\n")
        break

print(f"Question 14: Which security measure is most commonly used to authenticate a user at an ATM?")

while True:
    print('''
1.Fingerprint scanner
2.Security question
3.Personal Identification Number (PIN)
4.Facial recognition
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '3':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '3'.\n")
        break

print(f"Question 15: Which of the following functions is used to transform all elements in an iterable?")

while True:
    print('''
1.filter()
2.count()
3.sum()
4.map()
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '4':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '4'.\n")
        break

print(f"Question 16: What happens when same parameter is given as positional and keyword?")

while True:
    print('''
1.Uses both
2.Gives error
3.Takes positional
4.Takes keyword
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 17: Can two functions have the same name?")

while True:
    print('''
1.Only if parameters are different
2.Yes, always
3.Only in loops
4.No, that gives an error
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '1':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '1'.\n")
        break

print(f"Question 18: Which of the following is correct order?")

while True:
    print('''
1.keyword ? default ? positional
2.default ? keyword ? positional
3.positional ? keyword ? default
4.positional ? default ? keyword
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '4':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '4'.\n")
        break

print(f"Question 19: Can **kwargs accept any number of keyword args?")

while True:
    print('''
1.No
2.Yes
3.Only 1
4.Only fixed
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '2':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '2'.\n")
        break

print(f"Question 20: Which of the following statements is true?")

while True:
    print('''
1.Functions can’t return values
2.Functions can't be empty
3.Functions can have parameters
4.Functions must be recursive
''')
    op = input("Your Answer(1/2/3/4): ")

    if op == '3':
        count+=1
        print("✅Correct!\n")
        break
    else:
        print(f"❌Wrong! the correct answer is '3'.\n")
        break
    
print(f"🎯Your Final Score:{count}")
print(f"🎉 Great job! Keep practicing!")