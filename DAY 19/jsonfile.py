import json

with open('demo2.json','w') as file:
    data = [
        {'title':'python Basics','author':'Jhon Doe','Price':1499},
        {'title':'JAVA Basics','author':'Jhon Doe','Price':199},
        {'title':'HTML Basics','author':'Jhon Doe','Price':1399},
        {'title':'MYSQL Basics','author':'Jhon Doe','Price':1999}
        ]
    json.dump(data,file,indent = 4)

'''with open('demo2.json','r') as file:
    print(json.load(file))'''
