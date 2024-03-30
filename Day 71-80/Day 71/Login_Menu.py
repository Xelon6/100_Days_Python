import json
import os
import getpass
import secrets
import hashlib
import time

os.chdir(os.path.dirname(os.path.realpath(__file__)))

FILE_NAME="user_data.json"


def clear_console():
    """cleared console auf win und unix"""
    os.system('cls' if os.name == 'nt' else 'clear')



def menu():
    clear_console()
    print("Login System")
    print("1.) Register User\n2.) Login\n3.) Exit")

def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


def register():
    clear_console()
    salt = secrets.token_hex(8)
    username=input("Enter you Username\n> ")
    

    try:
        with open(FILE_NAME, "r", encoding="UTF-8") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = {}

    if username in users:
        print("User already exists")
        time.sleep(1.5)
    else:
        password=getpass.getpass("Enter your Password\n> ")
        new_pw=f"{password}{salt}"
        hashed_pw = hash_password(new_pw)
        users[username] = {'password': hashed_pw, 'salt': salt}

    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        json.dump(users, f)
        

def login():
    clear_console()
    try:
        with open(FILE_NAME, "r", encoding="UTF-8") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: No users registered yet")
        time.sleep(1.5)
        return

    print("Enter your Username")
    username = input("> ")
    if username in users:
        pw = getpass.getpass("Enter your Password\n> ")
        salt = users[username]['salt']
        password = f"{pw}{salt}"
        hashed_pw = hash_password(password)
        if hashed_pw == users[username]['password']:
            print("Successful Login")
            time.sleep(1.5)
        else:
            print("Error: Wrong Password")
            time.sleep(1.5)
    else:
        print("Error: Couldn't find your User")
        time.sleep(1.5)




    
def main():
    while True:
        menu()
        x=input("> ").lower().strip()
        if x in ["1","register"]:
            register()
        elif x in ["2","login"]:
            login()
        elif x in ["3","exit","quit"]:
            break


if __name__ == "__main__":
    main()