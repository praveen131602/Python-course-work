import csv

with open('sample.csv','r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)
