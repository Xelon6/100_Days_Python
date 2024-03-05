import os
import time

my_list = []

def printlist():
    counter = 0
    for item in my_list:
        counter += 1
        print(f"\33[35m{counter:>20}. {item}\33[0m")


while True:
    
    user_choice=input("Do you want to view, add or edit your to do list?\nTo quit please use exit\n")
    
    if user_choice.lower() == "edit":
        try:
            my_list.remove(input("Which item do you want to remove?\n"))
            time.sleep(1)
            os.system("cls")
        except ValueError:
            print("The item you have choosen is not in the list!")
    elif user_choice.lower() == "add":
        my_list.append(input("What do you want to add to your todo list?\n"))
        time.sleep(1)
        os.system("cls")
        
    elif user_choice.lower() == "view":
        printlist()
        
    elif user_choice.lower() in ["exit","quit","leave","bye"]:
        break
    
    else:
        print("Invalid command")
        
    