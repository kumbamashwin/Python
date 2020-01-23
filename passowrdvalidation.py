


password = input("Enter a password")

if len(password) in list(range(5,13)) and ('$' in password or '@' in password) and not password.isupper():
    print ("valid Passwrod")
else:
    print ("invalid Passowrd")
    
    
    