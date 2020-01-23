#decrypting the file
from cryptography.fernet import Fernet
import os
with open ("key.key", "r") as fkey:
    key = fkey.read()
    print(key)
    
inputfile = "properties_encrypted.conf"
outputfile = "properties.conf"

with open(inputfile, 'rb') as f:
    data = f.read()
    
    
fernet = Fernet(key)
encrypted =fernet.decrypt(data)

with open(outputfile, 'wb') as f:
    f.write(encrypted)

