T = (1,2,3,4,5,6,7,8,9,10)
print(T)
print(type(T))
print(dir(T))

print(T[4])
print(T[-2])
print(T[:])
print(T[2:])
print(T[4:7])
#print(T[-1][0])

L2 = (2,5,6,4,8)
print(sum(L2))
print(min(L2))
print(max(L2))
print(len(L2))

Fruits = ('Orange','Apple','Pineapple','Kiwi','Cherry')
print(max(Fruits))
print(min(Fruits))
print(len(Fruits))
#print(sum(Fruits))

St_L=[91,94,97,80,99,14,23]
St_L.sort(reverse=True)
print(St_L)
print(St_L[1])
St_L.sort()
print(St_L[-2])

L = [1,4,3,1,7,3,9,3,1]
UL= list(set(L))
print(UL)