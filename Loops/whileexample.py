# for a in range(10):
#     print(a)
#
# a=0
# while(a<=9):
#     print(a)
#     a+=1

#------------------------------------------------------------------------------------
# for a in range(1,11):
#     for b in range(1,11):
#         print(f"{a}*{b}={a * b}", end="")
#     print()
#
# a= 1
# while(a<=10):
#     b=1
#     while (b<=10):
#         print(f"{a}*{b}={a*b}",end="")
#         b+=1
#     print()
#     a+=1

#------------------------------------------------------------------------------------

# c=1
# for a in range(1,11):
#     for b in range(1,a+1):
#         if c%2==0:
#             print("even",end="")
#         else:
#             print("odd",end="")
#         c+=1
#     print()
#
# c=1
# a=1
# while a<=10:
#     b=1
#     while b<=10:
#         if c%2==0:
#             print("even",end="")
#         else:
#             print("odd",end="")
#         b+=1
#         c+=1
#     print()
#     a+=1

#----------------------------------------------------------------------------------

from hidden_number import num
flag = True
while flag:
    n= int(input("Enter a number: "))
    if n==num:
        print("You guessed correctly")
        flag = False
    elif n>num:
        print("You entered higher than the number")
    else:
        print("You entered lower than the number")

#----------------------------------------------------------------------------------

