try:
    a=int(input())
    if a<0:
        raise Exception("enter the positive value")

except Exception as e:
    print(f'error occured in :{e}')

else:
    print("no errors")
    
finally :
    print("end of the block")
