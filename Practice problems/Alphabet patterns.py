# 'A' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or col==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# 'B' alphabet using * pattern
n = int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == 0 or row ==0 and col<n-1 or row==n//2 and col < n-1 or row==n-1 and col < n-1 or col==n-1 and row!=0 and row != n//2 and row!= n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'C' alphabet using * pattern
n= int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row==0 or col == 0 or row == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'D' alphabet using * pattern
n= int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        if col == 0 or row ==0 and col<n-1 or row==n-1 and col < n-1 or col==n-1 and row!=0 and row!= n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'E' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'F' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'G' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == 0 or row == n-1 or (col == n-1 and row>=n//2) or (row==n//2 and col>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'H' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col==0 or col== n-1 or row==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'I' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row==0 or row== n-1 or col==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'J' alphabet using * pattern
n=int(input("Enter n: "))
for row in range(n):
    for col in range(n):
        if row==0 or col == n-1 or row == n-1 or (row == n-2 and col == 0) or (row == n-3 and col == 0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# 'K' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == 0 or row + col == n//2 or row-col == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'L' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col==0 or row== n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'M' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col==0 or col==n-1 or row==col and row <= n//2 or row+col==n-1 and row <= n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'N' alphabet using * pattern
n=int(input("Enter n: "))

for row in range (n):
    for col in range(n):
        if col==0 or col==n-1 or row==col:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

# 'O' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if ((row == 0 or row == n - 1) and 0 < col < n - 1) or \
           ((col == 0 or col == n - 1) and 0 < row < n - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 'P' alphabet using * pattern
n = int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n//2 or (col == n-1 and row <= n//2):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

# 'Q' alphabet using * pattern



# 'R' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == 0 or row == 0 or row == n//2 or row-col == n//2 or (col==n-1 and row<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'S' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row == n//2 or(col == 0 and row <= n//2) or(col == n-1 and row >= n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'T' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row == 0 or col == n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'U' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row == n-1 or col == 0 or col == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'V' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if (col == row or col + row == n-1) and row <= n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'W' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if col == 0 or col == n-1 or (row==col and row>=n//2) or (row+col==n-1 and row>=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# 'X' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if row == col or row+col == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'Y' alphabet using * pattern
n=int(input("Enter n: "))

for row in range(n):
    for col in range(n):
        if (col == n//2 and row>=n//2) or (row==col and row<=n//2) or (row+col==n-1 and row<=n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 'Z' alphabet using * pattern
n=int(input("Enter the size: "))

for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or row+col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()