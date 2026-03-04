products = ['car','shoe','shirt','handbags','laptop','facewash']
search = input("enter the item:")
if search in products:
    print(f"{search} is found !\ go and shop now")
else:
    print(f"{search}not found !\ go through another")
    
