name = input("enter the name:")
mobileno = int(input("enter the mobile number :"))
product_1 = input("enter the product_1 name :")
price_1 = int(input("enter the product_1 price"))
product_2 = input("enter the product_2 name")
price_2 = int(input("enter the product_2 price:"))
product_3 = input("enter the product_3 name")
price_3 = int(input("enter the product_3 price:"))

print(f"{name} your bill")
print(f"{product_1} : ${price_1}")
print(f"{product_2} : ${price_2}")
print(f"{product_3} : ${price_3}")

total_bill =price_1 + price_2 + price_3
print(total_bill)


            
