from cryptography.fernet import Fernet 
import hashlib
import base64
import os

def clear_history():
    os.system('cls' if os.name == 'nt' else 'clear')

def converting_password(password: str) -> bytes:
    key1 = password
    hashed_key = hashlib.sha256(key1.encode('utf-8'))
    hashed_key_digest = hashed_key.digest()
    base64_key = base64.b64encode(hashed_key_digest)
    return base64_key

def clear_file():
    data = open(filename, 'rb+')
    data.truncate(0)


#input for the base password, that comes back as a base64 key from the converting_passord() functions
clear_history()
key = (converting_password(input("Enter password (note that if you try decrypting using a wrong password the program may crash) :    ")))
f = Fernet(key)

filename = str(os.path.join(os.path.expanduser('~'), 'Documents'))+ r'\Manager.txt'
with open(filename, 'a+') as file:
    file.close()
    pass



def add_password():
    o_file = open(filename, 'rb')
    print(str(o_file))
add_password()
