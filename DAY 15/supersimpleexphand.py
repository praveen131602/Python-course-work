try:
    a= int(input())
    print(a[4])

except Exception as e:
    print(f'error occured in :{e}')

else:
    print("no errors")
    
finally :
    print("end of the block")
