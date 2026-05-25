#It is a single line function
#Syntax:
#o= lambda  argument (optional): expression (mandatory)

x= lambda: '-' *25
# print(x())

abe= lambda a,b : (a**2)+(b**2)+(2*a*b)
# print(abe(4,6))
# print(abe(5,7))

sum_of_three_number= lambda a=4,b=7,c=3: (a+b+c)
# print(sum_of_three_number(4,8,1))
# print(sum_of_three_number(5,2))
# print(sum_of_three_number(9))
# print(sum_of_three_number())

x1= lambda r:3.14*(r**2) #πr²
# print(x1(4))