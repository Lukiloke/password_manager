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


def encrypt_file():
    original_data = open(filename, "rb").read()
    encrypted_data = f.encrypt(original_data)
    deletion = open(filename,'r+')
    deletion.truncate(0)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)
    file.close()

def decrypt_file():
    encrypted_file = open(filename, "rb").read()
    decrypted_data = f.decrypt(encrypted_file)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)
        file.close()

def decrypt_variable_mode():
    encrypt_file = open(filename, 'rb').read()
    decrypted_data_vmode = f.decrypt(encrypt_file)
    out_vmode = decrypted_data_vmode.decode('utf-8')
    return out_vmode

def read_file_content():
    content = open(filename, "rb").read()
    content = content.decode('utf-8')
    return content

def write_file():
    data_w = "\n"+ input('Data to write:  ') 
    with open(filename,'ab') as file:
        file.write(data_w.encode('utf-8'))
        file.close()

def clear_file():
    data = open(filename, 'rb+')
    data.truncate(0)

def add_password():
    with open(filename,'rb') as f_read:
        o_data= f_read.read()
    domain = input("App/Site:   ")
    login_details = input("Login Id:    ")
    password = input("Password:     ")
    additionals = input("Additionals? Y/n :     ")
    if additionals == "Y":
        additional_data = input("Enter Additional infos you want to add with this site:   ")
    else:
        additional_data = ""

    if o_data:
        o_file_decrypted_bytes = f.decrypt(o_data)
        o_file_decrypted = o_file_decrypted_bytes.decode('utf-8')
    else:
        o_file_decrypted = ""

    new_entry =  "\n"+ domain + "   " + login_details + "   " + password + "   " + additional_data

    to_write = (o_file_decrypted + new_entry).encode('utf-8')
    with open(filename, 'wb') as file:
        file.write(f.encrypt(to_write))
    

clear_history()
key = (converting_password(input("Enter password (note that if you try decrypting using a wrong password the program may crash) :    ")))
clear_history()
f = Fernet(key)
path= str(os.path.join(os.path.expanduser('~'), 'Documents'))+ r'\Manager.txt'
with open(path, 'a+') as file:
    file.close()
    pass
 

filename = path
option_loop = 0
while option_loop == 0:
    options = input( "Here are the available command :\n$ encrypt\n$ decrypt\n$ decrypt_vmode\n$ add_password\n$ file_content\n$ write_file\n$ clear_file\n$ exit\n\n      $ ")
    if options == "encrypt":
        clear_history()
        encrypt_file()
        print(">     File successfully encrypted !")

    elif options == "decrypt_vmode":
        clear_history()
        print(">     "+decrypt_variable_mode())

    elif options == "decrypt":
        clear_history()
        decrypt_file()
        print(">     File successfully decrypted !")

    elif options == "file_content":
        clear_history()
        print('>     '+read_file_content())
        
    elif options == "write_file":
        clear_history()
        write_file()

    elif options == "clear_file":
        clear_history()
        clear_file()
        print(">     File size set to 0 ")

    elif options == "add_password":
        clear_history()
        add_password()

    elif options == "exit":
        break
        

    else:
        clear_history()
        print(">     "+"Command doesn't exist, try again.")

    input()
    clear_history()



print("hello world")
