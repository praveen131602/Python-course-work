def num():
    limit = int(input("enter the number :"))

    for i in range(1, limit + 1):
         n_squ = i * i
         nsqu_1 = n_squ + 1
         nsqum_1 = n_squ - 1
         nnn = n_squ + i
         nn_n = n_squ - i
         
         print(f'\nn : {i}')
         print(f'n**2 :{n_squ}')
         print(f'n**2+1 :{nsqu_1}')
         print(f'n**2 - 1 :{nsqum_1}')
         print(f'n**2 + n :{nnn}')
         print(f'n**2 - n :{nn_n}')


num()
