'''num1 = eval(input("enter num 1:"))
num2 = eval(input("enter num 2:"))
num3 = eval(input("enter num 3:"))
if num1 > num2 and num3:
    print(f'number one is grater :{num1}')
elif num2 > num3 and num1:
    print(f'number two is grater :{num2}') 
elif num3 > num1 and num2:
    print(f'number three is grater :{num3}')
else:
    print("three are same nuumbers")

year = int(input("enter the year :"))
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    print("leep year")
else:
    print("not a leep year")'''

a = int(input("enter the number :"))
b = int(input("enter the number :"))
print("\n")
symbol = input ("""
A = add
B = sub
C = mul
D = div
select option in capital letters :""")



if symbol == "A":
    print(a+b)
elif symbol == "B":
    print(a-b)
elif symbol == "C":
    print(a*b)
elif symbol == "D":
    print(a/b)
else:
    print("invalid option")'''
