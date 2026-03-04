n = int(input("enter the number :"))
for row in range(n):
        for col in range(n):
            if (row+col)%2==0:
                print(0,end=' ')
            else:
                print('X',end=' ')
        print()
        

