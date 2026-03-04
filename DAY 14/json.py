with open("demo.json","r") as file:
    data = json.load(file)

    for i in data:
        print(i)
