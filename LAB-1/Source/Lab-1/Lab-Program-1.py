import re

#enter you password using input in-built function
password = input("enter password tha needs to be validated:-")

flag = 0

#cindition loop to validate passsword
while True:
    if (len(password) < 6 or len(password) > 16) :
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[$@!*]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag = 0
        print("It is a valid Password")
        break

if flag == -1:
    print("It is not a valid password")








