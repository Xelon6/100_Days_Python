from dotenv import load_dotenv
import os
import getpass
os.chdir(os.path.dirname(os.path.realpath(__file__)))

load_dotenv()

admin_user=os.getenv("ADMINUSER").lower().strip()
admin_pw=os.getenv("ADMINPASS")

normal_user=os.getenv("NORMALUSER").lower().strip()
normal_pw=os.getenv("NORMALPW")

while True:
    print("Please enter your username")
    user = input("> ").lower().strip()

    if user == admin_user:
        print("Please enter your Password")
        pw = getpass.getpass("> ")
        if pw == admin_pw:
            print("Hello admin")
        else:
            print("Wrong Password")
    elif user == normal_user:
        print("Please enter your Password")
        pw = getpass.getpass("> ")
        if pw == normal_pw:
            print("Welcome normie")
        else:
            print("Wrong Password")
    else:
        print("Couldnt find the user")

    if input("To quit press x... ").lower().strip() == "x":
        break