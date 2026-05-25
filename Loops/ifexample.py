#false /0 will not go inside the loop

n= int(input("Enter a number: "))

if n>18:
    print("You are eligible to vote.")
else:
    print(f"You are not eligible to vote.You have to wait for {18-n} years.")

#----------------------------------------------------------------------------------------------

num = int(input("Enter a number: "))
if num==0:
    print("The number is zero.")
elif num<0:
    print("The number is negative.")
elif num>0:
    print("The number is positive.")

#---------------------------------------------------------------------------------------------

#ID = int(input("Enter the ID: "))
#name = input("Enter your name: ")
#m1 = int(input("Enter the m1: "))
#m2 = int(input("Enter the m2: "))
#m3 = int(input("Enter the m3: "))
#if m1<35 or m2<35 or m3<35:
#    if m1<35 and m2<35 and m3<35:
#        grade = "All Failed"
#    elif m1<35 and m2<35:
#        grade = "Failed in 1 & 2"
#    elif m2<35 and m3<35:
#        grade = "Failed in 2 & 3"
#    elif m1<35 and m3<35:
#        grade = "Failed in 1 & 3"
#    elif m1<35:
#        grade = "Failed in 1"
#    elif m2<35:
#        grade = "Failed in 2"
#    else:
#        grade = "Failed in 3"
#else:
#    grade = "All Passed"
#print(grade)

if True:
    print ("True")
if False:
    print("False")
if 14:
    print("Something else")
if 0:
    print("Zero")

L=[]
if L:
    print ("zyz")

n = int(input("Enter a number: "))
if n%2 == 0:
    print(f"Even Number {n}")
else:
    print(f"Odd Number {n}")


