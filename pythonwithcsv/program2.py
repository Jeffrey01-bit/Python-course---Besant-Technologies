import csv
with open('Myoutput.csv','r',newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)