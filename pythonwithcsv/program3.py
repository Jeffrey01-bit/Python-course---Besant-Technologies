import csv

a= int(input("Enter a number of students: "))
final_students = []
for i in range(a):
    st= []
    id = int(input("Enter your id: "))
    name = input("Enter your name: ")
    mark1 = int(input("Enter your mark1: "))
    mark2 = int(input("Enter your mark2: "))
    mark3 = int(input("Enter your mark3: "))
    total = (mark1 + mark2 + mark3)
    average = total / 3
    if total >= 250:
        Grade = 'A'
    elif total >= 200:
        Grade = 'B'
    else:
        Grade = 'C'
    st.append(id)
    st.append(name)
    st.append(mark1)
    st.append(mark2)
    st.append(mark3)
    st.append(average)
    st.append(Grade)
    final_students.append(st)
    print(final_students)
with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(final_students)