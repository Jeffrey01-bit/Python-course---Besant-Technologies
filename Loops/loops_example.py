# # Calculating the sum of positive and negative numbers in a list:
# l= [9,14,-21,14,-28,17,14,-14]
# p_num = 0
# n_num = 0
# for i in range(0,len(l)):
#     if l[i]>0:
#         p_num+=l[i]
#     else:
#         n_num+=l[i]
# print("Sum of positive numbers: ",p_num)
# print("Sum of negative numbers: ",n_num)
# print("Sum of total numbers: ",p_num+n_num)
#
# #--------------------------------------------------------------------------------------
# #print all the person whose key is above 18:
# namedict= {'xyz':25,
#            'abc':12,
#            'Abu':17,
#            'Sandy':37,
#            'Sam':47}
# print("Person whose key is above 18: ")
# for k,v in namedict.items():
#     if v>18:
#         print(k,v)

# --------------------------------------------------------------------------------------
#Find the 2nd occurrence of 4:
l= [1,4,2,3,9,4,7,2]
# # first_index= l.index(4)
# # second_index= l.index(4,first_index+1)
# # print(first_index)
# # print(second_index)
# print(l.index(4,l.index(4)+1))
#
# print(l[2])
# print(l[4])
# print(l[:])
# print(l[2:6])
# print(l[0:7:1])

#Store all even num in l1 and odd num in l2:
l1=[]
l2=[]
for i in range(0,len(l)):
    if l[i]%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
print(l1)
print(l2)