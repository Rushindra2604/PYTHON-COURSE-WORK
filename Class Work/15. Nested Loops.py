#star square pattern
for row in range(5):
    for col in range(5):
        print("*",end=' ')
    print()

#same number in row
for row in range(5):
    for col in range(5):
        print(row,end=' ')
    print()

#same numbers in column
for row in range(5):
    for col in range(5):
        print(col,end=' ')
    print()

#star pattern with left right angle triangle( |_ )
for row in range(5):
    for col in range(row+1):
        print("*",end =" ")
    print()

#star pattern with reverse left right angle triangle( | )
for row in range(5):
    for col in range(5-row):
        print("*",end=" ")
    print()


for row in range(5):
    for col in range(5-row-1):
        print(" ",end=" ")
    for col1 in range(row+1):
        print("*",end=" ")
    print()

for row in range(5):
    for col in range(row):
        print(" ",end=" ")
    for col1 in range(5-row):
        print("*",end=" ")
    print()

n=int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

n=int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or row+col==n-1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

n=int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == col or row+col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

