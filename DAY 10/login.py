for i in range(3):
    username=input("enter the user name :")
    password=input("enter the password :")
    if username == 'admin' and password == 'PFS48':
        print("login successful")
        break
else:
    print("account locked")
