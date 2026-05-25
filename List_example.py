L=[]
print(L)
print(type(L))
print(dir(L))
L1 = [1,9,13,2,7,8,4,3]
print(L1)

#List Indexing
print(L1[1])
print(L1[3], L1[-3], L1[2])

#List Slicing
print(L1[:])
print(L1[:3])
print(L1[2:])
print(L1[2:6])

#List Append
L2= []
L2.append(8)
print(L2)
L2.append(14)
L2.append(17)
print(L2)
#List Insert
L2.insert(0,111)
L2.insert(2,15)
print(L2)
#List Extend
L2.extend(L1)
print(L2)
#List Copy
L3= L2.copy()
print(L3)
#List Clear
L3.clear()
print(L3)
#List Sort
L1.sort()
print(L1)
L1.sort(reverse=True)
print(L1)
#List Reverse
L2.reverse()
print(L2)
#List Pop
L4=[1,9,11,12,13]
L4.pop()
print(L4)
L4.pop()
#List Remove
L4.remove(9)
print(L4)
#List Count
L5= [1,4,2,2,2,4]
print(L5.count(2))
print(L5.count(4))
#List Index
print(L2)
print(L2.index(8))
print(L2.index(3))

#Set
S = set()
print(type(S))
print(dir(S))

S1={'A','B','C','D'}
print(S1)
#Add
S1.add('Z')
S1.add('Z')
print(S1)
#Copy
S2= S1.copy()
print(S2)
#clear
S2.clear()
print(S2)

Customer_2024 = {'A','B','C','D'}
Customer_2025 = {'Z','F','G','B','C'}
Customer_2026 = {'A','B','F','H','J'}
#Union
O = Customer_2024.union(Customer_2025)
print(O)
O1= Customer_2024.union(Customer_2025,Customer_2026)
print(O1)
#Intersection
O2 = Customer_2024.intersection(Customer_2025,Customer_2026)
print(O2)
#Difference
O3 = Customer_2024.difference(Customer_2025)
print(O3)
O3 = Customer_2025.difference(Customer_2024)
print(O3)
#Symmetric difference
O4 = Customer_2024.symmetric_difference(Customer_2025)
print(O4)

#Remove
S4 = {1,4,9,11}
#S4.remove(13)
print(S4)
#Discard
S4.discard(13)
print(S4)
#pop
S4.pop()
print(S4)

A = {1,2,3,4,5}
B = {1,2,3}
print(A.issuperset(B))
print(A.issubset(B))
#isdisjoint
X = {1,2,3}
Y = {4,5,6}
print(X.isdisjoint(Y))