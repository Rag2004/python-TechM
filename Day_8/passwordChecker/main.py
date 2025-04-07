password=input("Enter Password: ")
import re

if len(password)>8:
    if re.search(r'[A-Z]',password):
        if re.search(r'[a-z]',password):
            if re.search(r'[0-9]',password):
                if re.search(r'[!@#$%^&*()-]',password):
                    print("Strong Password")
                else:
                    print("Medium Password")
            else:
                print("Medium Password")
        else:
            print("Medium Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")                                    