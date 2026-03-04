with open('sample.text','r+') as file:
    file.write("\nfile operation")
    file.seek(0)
    print(file.read())
