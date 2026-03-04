data={
1:{'product':'Rice','price':60},
2:{'product':'Wheat Flour','price':40}, 	  		 
3:{'product':'Sugar','price':80},		 
4:{'product':'Milk','price':25},
5:{'product':'Eggs (12 pcs)','price':70},
6:{'product':'Cooking Oil','price':130},
7:{'product':'Tea Powder','price':90},
8:{'product':'Salt','price':20},
9:{'product':'Bread','price':30},
10:{'product':'Soap','price':25},
}

print('Index'.ljust(7,' '),'Product Name'.ljust(20,' '),'Price'.ljust(10,' '))
for i in data:
    print(str(i).ljust(7,' '),data[i]['product'].ljust(20,' '),str(data[i]['price']).ljust(10,' '))



indexes = list(map(int,input("Enter the indexes: ").split()))


print("Bill".center(30,'-'))
total_bill=0
for i in indexes:
    print(f'''{data[i]["product"]}
          {data[i]["price"]}*{indexes.count(i)}
          = {data[i]["price"]*indexes.count(i)}''')
    total_bill+= data[i]["price"]*indexes.count(i)
    s.add(i)

print(f"Your Bill: {total_bill}")


