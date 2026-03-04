class Flipkart:
    
    discount = 10

    @classmethod
    def updatediscount(cls,newdiscount):
        cls.discount = newdiscount

    def userinfo(self,name,phonenumber):#instant method
        self.name = name #instant attribute
        self.phonenumber = phonenumber
        print(f'Username:{self.name}')
        print(f'Phone number : {self.phonenumber}')


    @staticmethod
    def banner ():
        print("Welcome to the flipkart\n10% discount is going on, shop now")

praveen = Flipkart()
praveen.userinfo('praveen',98775645)

praveen.updatediscount(30)
Flipkart.updatediscount(40)

praveen.banner()
Flipkart.banner()
        
sapnil = Flipkart()
sapnil.userinfo('sapnil',98775645)

sapnil.updatediscount(30)
Flipkart.updatediscount(40)

sapnil.banner()
Flipkart.banner()

saaketh = Flipkart()        
saaketh.userinfo('saaketh',98775645)

saaketh.updatediscount(30)
saaketh.updatediscount(40)

saaketh.banner()
Flipkart.banner()
