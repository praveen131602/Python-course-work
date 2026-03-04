try:
    a=22
    if a>10:
        print("good")

except NameError:
    print("a is not defined")
    
except ValueError:
    print("Enter the requested data type")
    
except TypeError:
    print("data is not found")

except ZeroDivisionError:
    print("can't divide with zero")

except IndexError:
    print("The index is not present")

except KeyError:
    print("in dict this key is not present")
    
else:
    print("no errors")

finally:
    print("end of the block")

