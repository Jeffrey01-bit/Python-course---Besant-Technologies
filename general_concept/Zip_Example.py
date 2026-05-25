a= [4,9,5,8,3,9]
b= [7,3,5,1,5]
o= list(zip(a,b))
print(o)
o1= set(zip(a,b))
print(o1)
o2= dict(zip(a,b))
print(o2)
weekday= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekday_type= ['Working','Working','Working','Working','Working','Holiday','Holiday']
weekday_num= [1,2,3,4,5,6,7]
week = list(zip(weekday,weekday_type,weekday_num))
print(week)
week1 = set(zip(weekday,weekday_type,weekday_num))
print(week1)
# W3 = dict(zip(weekday,weekday_type,weekday_num))
# print(W3)
a,b,c = list(zip(*week))
print(a)
print(b)
print(c)