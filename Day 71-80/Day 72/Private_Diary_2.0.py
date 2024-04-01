import os
import time
import json
import hashlib
import getpass
import datetime
import secrets

FILE_NAME_DIARY = "diary.entries"
os.chdir(os.path.dirname(os.path.realpath(__file__)))
diary = {}

def clear_console():
    """cleared console auf win und unix"""
    os.system('clear' if os.name == 'posix' else 'cls')

def save_to_file(file_name,data):
    '''save to file'''
    with open(file_name,"w",encoding="UTF-8") as f:
        json.dump(data,f)

def check_for_file(file_name):
    '''schaut ob file da is wenn nicht ladet leere list'''
    global diary
    try:
        with open(file_name, "r", encoding="UTF-8") as file:
            diary = json.load(file)

    except FileNotFoundError:
        print("No existing File starting with a blank one")
        time.sleep(1.5)
        clear_console()

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

def add_user(username,password):
    salt = secrets.token_hex(8)
    new_pw = f"{password}{salt}"
    hashed_password = hash_password(new_pw)
    FILE_NAME = 'user_data.json'
    user_data = {}
    user_data[username] ={'password':hashed_password,'salt':salt} 
    
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, 'w',encoding="UTF-8") as file:
            json.dump(user_data,file)
            print("\n[+] Set Password\n")
    else:
        with open(FILE_NAME, 'x',encoding="UTF-8") as file:
            json.dump(user_data,file)
            print("\n[+] Set Password\n")


def login():
    FILE_NAME = 'user_data.json'
    attempts = 0
    while True:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME,'r',encoding='UTF-8') as file:
                user_data = json.load(file)
            while True:
                if attempts < 3:
                    username = input("Please enter your username\n> ")
                    if username in user_data:
                        entered_password = getpass.getpass("Please enter your Password to login\n> ")
                        password = f"{entered_password}{user_data[username]['salt']}"
                        stored_password = hash_password(password)
                        if stored_password == user_data[username]['password']:
                            return True
                        else:
                            clear_console()
                            attempts += 1
                            print("You entered the wrong password")
                            time.sleep(1)
                            continue
                    else:
                        print("You have entered an invalid username")
                else:
                    clear_console()
                    print("You have entered the password wrong 3 Times")
                    time.sleep(1)
                    exit()
                
        else:
            print("You haven't created a user yet please create one")
            username=input("Username: ")
            password = getpass.getpass("Password: ")
            add_user(username,password)

def menu():
    print("Welcome to your personal Diary")
    print()
    print("1.) add Diary Entry\n2.) View Diary Entries\n3.) Exit\n")

#speicher die diary entries mit dem timestamp als key
def add():
    timestamp = str(datetime.datetime.now())
    diary_entry=input("What did you do today?\n> ")
    diary[timestamp]=diary_entry

def view():
    clear_console()
    entries = list(diary.items())[::-1]
    for timestamp,values in entries:
        print(f"Your Diary entry on the {timestamp}")
        print()
        print(f"{values}")
        print()
        choice = input("press y to see another one press anythin else to quit\n> ").lower().strip()
        if choice != "y":
            clear_console()
            break
        clear_console()

    

def main():
    '''main Funktion'''
    check_for_file(FILE_NAME_DIARY)
    while True:
        clear_console()
        logged_in = login()
        
        while True:
            if logged_in is True:
                clear_console()
                menu()
                x = input("> ").lower().strip()
                if x in ["1","add"]:
                    add()
                    save_to_file(FILE_NAME_DIARY,diary)
                elif x in ["2","view"]:
                    view()
                    
                elif x in ["3","exit"]:
                    clear_console()
                    print("Goodbye")
                    save_to_file(FILE_NAME_DIARY,diary)
                    time.sleep(1)
                    exit()


if __name__ == "__main__":
    main()
