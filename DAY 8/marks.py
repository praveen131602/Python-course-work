n=int(input("enter the number of students: "))

names,gpas=[],[]
max_val=0
max_name=' '

min_val=0
min_name=' '

for i in range(n):
    print(f"-------------------student{i+1}--------------")
    name = input("enter the names: ")
    gpa = float(input("enter the gpa: "))

    if gpa>max_val:
        max_name=name
        max_val=gpa

    if gpa<min_val:
        min_name=name
        max_val=gpa

    names.append(name)
    gpas.append(gpa)

print(f'{"Names"}.ljust(15){"GPA".ljust(15)}')
print('-'*20)
    
for i in range(len(names)):
    print(f'{names[i].ljust(14)}| {str(gpas[i]).ljust(5)}')

print(names,gpas)
