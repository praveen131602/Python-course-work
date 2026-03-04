data={
1: {'product':'rice','price':69},
2: {'product':'tea','price':67},
3: {'product':'bread','price':20},
4: {'product':'eggs','price':690},
5: {'product':'salt','price':56},
6: {'product':'soap','price':34},
7: {'product':'shampoo','price':60},
8: {'product':'creatine','price':70},
9: {'product':'chiken','price':30},
10: {'product':'milk','price':40},
}
print(s.inmiddle("Your Bill")('-'*7)
for i in data:
    print(str(i).ljust(7,' '),
