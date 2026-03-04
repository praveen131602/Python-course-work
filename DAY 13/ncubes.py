def num():
    limit = int(input("enter the number :"))

    for i in range(1, limit+1):
                nc = i*i*i
                nc1 = nc +1
                ncm1 = nc - 1
                ncn = nc + i
                ncmn = nc - i

                print(f'\n n :{i}')
                print(f'n**3 : {nc}')
                print(f'n**3 + 1 : {nc1}')
                print(f'n**3 - 1 :{ncm1}')
                print(f'n**3 + n :{ncn}')
                print(f'n**3 - n :{ncmn}')

num()
