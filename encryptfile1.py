from cryptography.fernet import Fernet
import os
key = Fernet.generate_key()
############## creating the key and writing the key to key.key
file = open('key.key', 'wb')
file.write(key) # The key is type bytes still
file.close()

inputfile =  "properties.conf"   # original file
outputfile = "properties_encrypted.conf"   # encrypted file
## reading the original file
with open(inputfile, 'rb') as f:
    data = f.read()

##### ecnrypt the string to encrypted format
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# writing the encrypted string to the file
with open(outputfile, 'wb') as f:
    f.write(encrypted)
#  deleting the original file
os.rename(inputfile,outputfile)    
