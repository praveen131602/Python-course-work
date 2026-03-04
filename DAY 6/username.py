name = input("enter the name:")
dob = input("enter the dob [YYYY-MM-DD] :")

username = name[:2] + name[-2:] + dob[-2:] + dob[2:4]

print(f"Hii {name} , your Username : {username}")
