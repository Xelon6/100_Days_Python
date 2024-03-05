import os
import time

listOfEmail = []

def prettyPrint():
    os.system("cls")
    print("listOfEmail")
    print()
    counter = 1
    for emails in listOfEmail:
        print(f"{counter}: {emails}")
        counter += 1
    time.sleep(1)

def spam():
    if len(listOfEmail) >= 10:
        most = 10
    else:
        most = len(listOfEmail)
        
    for i in range(0, most):
        print(f"""Email {i+1}

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't, we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
        time.sleep(1)
        os.system("cls")

while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        spam()
    time.sleep(1)
    os.system("cls")
