'''for num in range(1,10,2):
    print(num)'''
'''List = ["soap", 100, 9.09, True, "shampoo"]
for sarukul in List:
    print(sarukul)'''

'''Name = "ABHI"
for i in Name:
    print(i)'''

'''List = ["soap", 100, 9.09, True, "shampoo"]
for sarkulu in range(len(List)):
    print(sarkulu)'''

'''i = 1
while i <= 5:
    print(i)
    i = i + 2'''
'''for i in range(6):
    print(i)
    for j in range(5):
        print(j, end = "  ")'''
'''for i in range(5):
    if i == 2:
        continue   # skips printing 2
    print(i)'''
'''n = int(input("enter the number :"))
for tables in range(1,n):
    for number in range(1,11):
        print(f'{tables} x {number} = {tables*number}')
    print()'''

'''List =  ["Apple", "Banana", "Mango"]
for sarukulu , names in enumerate(List):
    print(sarukulu,names)'''
'''List = [12, 13, 15, 16, 14]
Even = []
Odd = []
for i in List:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)
print("Even", Even)
print("Odd", Odd)'''

Dic = {"Name" : "Abhi", "Age" : 23, "Add" : "HYD"}

for key, value in enumerate(Dic.items()):
    print(key, value)
        
