import random
import time
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def clear_console():
    """Clear console"""
    os.system('clear' if os.name == 'posix' else 'cls')


def save_idea(idea):
    """save idea to file"""
    f = open("my.ideas","a+",encoding="UTF-8")
    f.write(f"{idea}\n")
    f.close()


def rand_idea():
    """random idea output"""
    f = open("my.ideas","r",encoding="UTF-8")
    ideas = f.readlines()
    idea = random.choice(ideas)
    return idea


def main():
    """main function"""
    while True:
        clear_console()
        print("Do you want to\n1.) add an idea\n2.) read a random idea of yours\n3.) exit")
        choice = input("> ").lower().strip()
        if choice in ["add","1"]:
            clear_console()
            save_idea(input("What idea do you want to save?\n> ").strip())
            clear_console()
        elif choice in ["view","read","2"]:
            clear_console()
            print(rand_idea())
            time.sleep(2)
            clear_console()
        elif choice in ["exit","3","quit"]:
            clear_console()
            print("See you next time")
            time.sleep(1)
            clear_console()
            break
        else:
            print("Please choose a valid option")
    
    
if __name__ == "__main__":
    main()