gallery = ["beach.png","mountain.png","party.jpg","selfie.jpg","birthday.png","concert.jpg"]
for i in range(len(gallery)):
    print(f'{i+1}.{gallery[i]}')

s= set(map(int,input("Enter the pic ids:").split(',')))

for i in s:
    print(gallery[i-1])