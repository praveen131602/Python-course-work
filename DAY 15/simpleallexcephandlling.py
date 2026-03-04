try:
    a=a+'8'
    print(a[4])

except(NameError,ValueError,TypeError,ZeroDivisionError,SyntaxError,IndexError,KeyError) as e:
    print(f'Error Occured:{e}')

else:
    print("End of the Block")
