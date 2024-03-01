import getpass

def login():
    versuche={
        3:"dreimal",
        2:"zweimal",
        1:"einmal",
        0:"error"
    }
    while True:

        username=input("Bitte gib deinen Benutzernamen ein: ")
        if username.lower() == "david":
            for i in range(4,0,-1):
                password=getpass.getpass("Bitte gib dein Password ein: ")
                if password == "123":
                    print("Login succesful")
                    break
                else:
                    if i > 1:
                        print("Password ist falsch du kannst es noch",versuche[i-1],"versuchen")
                    else:
                        print("Password zu oft falsch eingegeben")
        else:
            print("Login Infos Falsch")
            continue
        break
login()
