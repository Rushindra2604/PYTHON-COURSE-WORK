import random

print('1.Rock')
print('2.Paper')
print('3.Scissors')

while True:
    ch=int(input("Enter your choice(0-Exit): "))
    if ch==0:
        print("Game Over")
        break
    elif ch==1:
        com=random.randint(1,3)
        if com==1:
            print("computer choice:",com)
            print('Tie both choose the rock')
        if com==2:
            print("computer choice:",com)
            print('Computer Wins')
        if com==3:
            print("computer choice:",com)
            print('Congrats You Win')
    elif ch==2:
        com=random.randint(1,3)
        if com==1:
            print("computer choice:",com)
            print('Congrats You Win')
        if com==2:
            print("computer choice:",com)
            print('Tie both choose the paper')
        if com==3:
            print("computer choice:",com)
            print('Computer Wins')
    elif ch==3:
        com=random.randint(1,3)
        if com==1:
            print("computer choice:",com)
            print('Computer Wins')
        if com==2:
            print("computer choice:",com)
            print('Congrats You Win')
        if com==3:
            print("computer choice:",com)
            print('Tie both choose the scissors')

    else:
        print("Invalid Move")
        
        
