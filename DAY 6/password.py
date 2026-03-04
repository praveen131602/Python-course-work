pwd = input("enter the passward :")
if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("upprer")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
    else:
        s.add("spcl char")
if len(s)==4:
    print("strong password")
else:
    print("weak password")
    
