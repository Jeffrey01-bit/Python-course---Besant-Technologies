print("Example 1: ")
for R in range (1,10):
    if R==5:
        for C in range (1,5):
            print('*',end =' ')
        print()
    else:
        for b in range (1,5):
            if b in(1,4):
                print('*',end =' ')
            else:
                print(' ',end =' ')
        print()
#-------------------------------------------------------------------------------------------
print("Example 2: ")
for R in range (1,10):
    if R in (1,5,9):
        for C in range (1,5):
            print('*',end =' ')
        print()
    else:
        for b in range (1,5):
            if b == 1:
                print('*',end =' ')
            else:
                print(' ',end =' ')
        print()
#--------------------------------------------------------------------------------------------
print("Example 3: ")
for R in range (1,10):
    if R in (1,5):
        for C in range (1,5):
            print('*',end =' ')
        print()
    elif R in(2,3,4):
        for b in range (1,5):
            if b in (1,4):
                print('*',end =' ')
            else:
                print(' ',end =' ')
        print()
    else:
        for b in range (1,5):
            if b ==1:
                print('*',end =' ')
            else:
                print(' ',end =' ')
        print()
