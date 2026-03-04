'''names =['abhi','akhi','dinesh','bharth','nandhan']

for i in enumerate(names):
    print(f'{i[0]}.{i[1]}')'''

i=0
while i<len(names):
    print(f'{i+1}.{names[i]}')
    i+=1
