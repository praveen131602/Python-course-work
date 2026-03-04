data = {
    123456 : {'pin':1234,'balance' :5000,'history':[]},
    234567 : {'pin':12345,'balance' :5000,'history':[]},
    345678 : {'pin':12346,'balance' :5000,'history':[]},
    456789 : {'pin':12347,'balance' :5000,'history':[]}
    }


def menu():
    print('1.check balance')
    print('2.diposit')
    print('3.withdraw')
    print('4.set pin')
    print('5.view transections')
    print('6.exit\n')



print("Welcome to ATM")

acc = int(input("enter the account number :"))
pin = int(input("enter the pin :"))

if acc in data and data[acc]['pin']==pin:
          print("login successfull")
while True:
    menu()
    ch =int(input("enter the choise :"))
    if ch == 6:
            print("thankyou")
            break
else:
    print("invalid login.try again")
