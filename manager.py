from cryptography.fernet import Fernet 
import hashlib
import base64
import os
main_list = []

def clear_history():
    os.system('cls' if os.name == 'nt' else 'clear')

def converting_password(password: str) -> bytes:
    key1 = password
    hashed_key = hashlib.sha256(key1.encode('utf-8'))
    hashed_key_digest = hashed_key.digest()
    base64_key = base64.b64encode(hashed_key_digest)
    return base64_key

clear_history()
key = (converting_password(input("Enter password (note that if you try decrypting using a wrong password the program may crash) :    ")))
f = Fernet(key)
filename = r"C:\Users\User\Desktop\VisualStudio\password_manager\test.txt"
with open(filename, 'a+') as file:
    file.close()
    pass



def add_password():
    domain = input("App/Site:   ")
    login_details = input("Login Id:    ")
    password = input("Password:     ")
    additionals = input("Additionals? Y/n :     ")
    if additionals == "Y":
        additional_data = "   " + input("Enter Additional infos you want to add with this site:   ")
    else:
        additional_data = ""
    new_entry =   domain +"   " + login_details + "   " + password + additional_data
    main_list.append(new_entry)


def clear_file():
    data = open(filename, 'rb+')
    data.truncate(0)
    

def search(item): #search an item in the main list and show it
    with open(filename,'rb') as file:
        a = 0
        for i in main_list :
            if item.lower() in i.lower() :
                print(i)
                #print("\nItem position for deletion:   " + str(main_list.index(i)))
                delete_it = input("\nDelete it   Y/n:   ")
                if delete_it == "Y":
                    confirm_deletion = input("Enter Del_Credential to confirm deletion: ")
                    if confirm_deletion == "Del_Credential":
                        main_list.pop(main_list.index(i))
                        print("> Item Deleted !")
                    else:
                        pass
                else:
                    pass
                a = 1
        if a == 0:
            clear_history()
            print("Item Not Found...")


def all_content(): #shows every credentials saved in the file
    file_content = '\n'.join(main_list)
    print(file_content)

def debug():
    debug_options = input("Available options:\n$ clear_file\n\n      $ ")
    if debug_options == "clear_file":
        clear_file()
        main_list.clear()
        clear_history()
        print(">     File size set to 0 ")



with open(filename, "rb") as file :   #So yeah, this just store file content in a list
    o_data = file.read()
    if o_data:
        decrypted_file_content = f.decrypt(o_data).decode('utf-8')
        main_list = decrypted_file_content.splitlines()
    else:
        o_data = ''

    main_list = [item.replace('\n', '') for item in main_list]

option_loop = 0
while option_loop == 0:
    options = input( "Here are the available command :\n$ list_all\n$ add_password\n$ clear_file\n$ search & delete\n$ debug\n$ exit\n\n      $ ")

    if options == "clear_file":
        clear_history()
        clear_file()
        print(">     File size set to 0 ")

    elif options == "list_all":
        clear_history()
        all_content()

    elif options == "add_password":
        clear_history()
        add_password()

    elif options == "debug":
        clear_history()
        debug()

    elif options == "exit":
        break

    elif options == "":
        pass

    elif options == "search":
        clear_history()
        search(input("Item to search:   "))

    else:
        clear_history()
        print(">     "+"Command doesn't exist, try again.")

    input()
    clear_history()

deletion = open(filename, 'rb+')
deletion.truncate(0)

with open(filename, 'wb') as file:
    to_write = '\n'.join(main_list).encode('utf-8')
    to_write_encoded = f.encrypt(to_write)
    file.write(to_write_encoded)
