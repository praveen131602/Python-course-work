try:
    a=22
    if a>10:
        print("good")

except NameError:
    print("a is not defined")
else:
    print("no errors")

finally:
    print("end of the block")
