#Benutzt Replit DB wird also nur auf Replit funktionieren
from replit import db
import datetime
import os
import time



def clear_console():
    """cleared console auf win und unix"""
    os.system('clear' if os.name == 'posix' else 'cls')

def add():
    clear_console()
    timestamp=datetime.datetime.now()
    tweet =input("What should your tweet say?\n> ")
    key = f"message{timestamp}"
    db[key] = tweet
    print()
    print("Added tweet")
    time.sleep(1)
    clear_console()

def view():
    tweets = db.prefix("message")
    tweets = tweets[::-1]
    counter = 0
    for i in tweets:
        print(db[i])
        print()
        time.sleep(0.3)
        counter+=1
        if(counter%10==0):
            carryOn = input("Next 10?: ")
            if(carryOn.lower()=="no"):
                break
    time.sleep(1)
    os.system("clear")


def menu():
    print("Welcome to your personal Twitter :)")
    print()
    print("1.) Add tweet")
    print("2.) View Tweets")
    print("3.) Exit")
    x=input("> ").lower().strip()
    if x in ["1","add","tweet"]:
        return 1
    elif x in ["view","2"]:
        return 2
    elif x in ["3","exit"]:
        clear_console()
        print("Goodbye")
        time.sleep(1.5)
        exit()        
    else:
        print("Invalid option")


def main():
    while True:
        clear_console()
        choice = menu()
        if choice == 1:
            add()
        if choice == 2:
            view()


if __name__ == "__main__":
    main()
