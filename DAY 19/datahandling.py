try:
    with open('data.txt','r') as file:
        print(len(file.readlines()))
except FileNotFoundError:
    print("data.txt does not exit")
