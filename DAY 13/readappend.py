file = open('sample.text','w+')

file.write("\nfile operation")
file.seek(0)
print(file.read())

file.close()
