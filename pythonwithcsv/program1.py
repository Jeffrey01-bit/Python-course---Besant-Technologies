import csv
id= int(input("Enter your id: "))
name= input("Enter your name: ")
mark1=int(input("Enter your mark1: "))
mark2= int(input("Enter your mark2: "))
mark3= int(input("Enter your mark3: "))
total= (mark1+mark2+mark3)
average= total/3
if total >= 250:
    Grade='A'
elif total >= 200:
    Grade='B'
else:
    Grade='C'
# print(id,name,mark1,mark2,mark3,total,average,Grade)

# with open('Myoutput.csv','a') as file:
#     writer = csv.writer(file)
#     writer.writerow([id,name,mark1,mark2,mark3,total,average,Grade])
# with open('Myoutput.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow([id,name,mark1,mark2,mark3,total,average,Grade])
with open('Myoutput.csv','a',newline='') as file:
    writer = csv.writer(file)
    writer.writerow([id,name,mark1,mark2,mark3,total,average,Grade])