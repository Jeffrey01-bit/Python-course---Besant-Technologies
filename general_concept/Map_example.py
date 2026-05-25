from Lambda_Example import *
from Function_example import *

usernmaelist = ['admin','root','ABC','DEF','admin']
passwordlist = ['root','admin','123','456','admin']

# applying logincheck using map
O = list(map(logincheck, usernmaelist, passwordlist))
print(O)

O1 = list(zip(usernmaelist, passwordlist, O))
print(O1)