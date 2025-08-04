data={
    1:{"name":"Rice","price":60},
    2:{"name":"Wheat","price":50},
    3:{"name":"Flour","price":45},
    4:{"name":"Sugar","price":40},
    5:{"name":"Milk","price":25},
    6:{"name":"Cooking oil","price":130},
    7:{"name":"Biscuits","price":30},
    }
print(data) # prins

for i in range(1,8):
    print(f'{i}.{(data[i]["name"]).ljust(15," ")}:{data[i]["price"]}') # prints with space in table way


items=list(map(int,input("Enter the item indexes: ").split()))
    
total=0
ids=set()
for i in items:
    if i not in ids:
        co=items.count(i)
        total+=(data[i]["price"]*co)
        print(f'{data[i]["name"]}-{co}*{data[i]["price"]}={data[i]["price"]*co}')
    ids.add(i)

print("Total Bill:",total)