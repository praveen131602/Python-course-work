n = int(input("enter the number :"))
for row in range(n):
    for spc in range(row+1):
        print(' ',end=' ')
    for col in range(n-row-1):
        print('*',end=' ')
    print()

