'''Dic = {"Name" : "abhi","Age": 22,"Address" : "HYD"}

Dic["Phone","King"] = 9059131359,"raju"
Dic["Height"] = 5.8

print(Dic)'''

'''List = ["abhi", "akhi", "anish"]

Dic={}
for i in List:
    Dic[i] = i[::-1]
print(Dic)'''

'''List = ["abhi","akhi","anish"]

Dic = {}
for i in List:
    rev = ""
    for j in i:
        rev = j+rev
    Dic[i] = rev
print(Dic)'''


'''String = "Python"
for i in range(len(String)):
    print(i, String[i])'''

'''List = ["apple", "banana", "mango", "kiwi"]
List2 = []
for i in List:
    List2.append(i[::-1])
print(List2)'''

'''num = 6
Sum = 0
for i in range(1,num):
    if num % i == 0:
        Sum += i
if num == Sum:
    print("perfect number")
else:
    print("not a perfect number")'''

num = 1234
temp = num
Rev = 0
while num > 0:
    rem = num % 10
    Rev = (Rev*10) + rem
    num = num // 10

print(f"The orginal Number {temp} and the reverse number is {Rev} ")
