n = int(input("enter the number :"))
for row in range(n):
        for col in range(n):
            if row==0 or row==n-1 or row+col==n-1:
                 print('*',end=' ')
            else:
                 print(' ',end=' ')
        print()
        
