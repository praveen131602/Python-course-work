import csv

with open("samples.csV","w",newline=" ")as file:
    writer = csv.writer(file)
    writer.writerow(["6","Nikhil","JFS"])
    
