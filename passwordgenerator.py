#Password Generator
import random
def passwordGenerator():
    lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m''n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_characters=['@','$','&','*','!','^',"#"]
    numeric_chars=['1','2','3','4','5','6','7','8','9','10']
    password=random.choice(lower_case)+random.choice(upper_case)+random.choice(special_characters)+random.choice(numeric_chars)
    if password=="pR*4" or password=="kL$5" or password== "rT!6":
        print("correct password")
    else:
        print("password not matched")
    return password
print(passwordGenerator())
