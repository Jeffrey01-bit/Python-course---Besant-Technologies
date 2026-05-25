print("Print all numbers till you encounter a negative number:")
L= [1,4,9,10,11,-8,17,23,44]
# print(len(L))
for  a in range (len(L)):
#    print(L[a])
    if L[a]<0:
        break
    else:
        print(L[a])

# Print only all positive no:
print("Print only all positive no:")
L= [1,4,9,10,11,-8,17,-23,44]
# print(len(L))
for  a in range (len(L)):
#    print(L[a])
    if L[a]<0:
        continue
    else:
        print(L[a])