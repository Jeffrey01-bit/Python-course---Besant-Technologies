def logincheck(username, password):
    # predefined valid credentials
    valid_users = {
        "admin": "admin",
        "root": "root",
        "ABC": "123",
        "DEF": "456"
    }

    # check if username exists and password matches
    if username in valid_users and valid_users[username] == password:
        return f"{username} -> Login Successful"
    else:
        return f"{username} -> Login Failed"

def sumofnumbers(*args):
    sum=0
    for n in args:
        sum+=n
        print(sum)
    return sum
O= sumofnumbers(1,2,3,4,5,6,7,8,9,10)
print(O)

def concatstrings(*args):
    string=""
    for n in args:
        string+=n
        string+="-"
        print(string)
    return string
O2= concatstrings('ABC','DEF','GHI','JKL','MNO')
print(O2)

def keywordarguments(**args):
    for k,v in args.items():
        print(f"{k} and value = {v}")
keywordarguments(id= 1, name= 'Jef',Location= 'Chennai')