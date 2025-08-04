#For Else
l = ['smartphone','laptop','airpods','shoes']
for i in l:
    if i=='airpods':
        continue
    print(i.center(20,'_'))
else:
    print('End of the items')

#While Else
bullets=10
while bullets>0:
    if bullets==5:
        print("Dead")
        break
    print(f'{bullets} are left to shoot()')
    bullets-=1
else:
    print("Game over")

#prime numbers

fact=0
n=int(input("Enter the num: "))
for i in range(2,n+1):
    if n%i==0:
        fact+=1
if fact==1:
    print(f"{n} is prime number\nFactors count={fact}")
else:
    print(f"{n} is not a prime number\nfactors count={fact}")

#Reduced code for prime number

fact=0
n=int(input("Enter the num: "))
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f"{n} is prime number\nFactors count={fact}")
else:
    print(f"{n} is not a prime number\nfactors count={fact}")