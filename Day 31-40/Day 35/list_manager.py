import os
import time

my_list = []

def printlist():
    counter = 0
    for item in my_list:
        counter += 1
        print(f"\33[35m{counter:>20}. {item}\33[0m")


while True:
    
    os.system("cls")
    print("\33[35mList Manager\33[0m\n")
    print("To view all items in the list type \"view\"")
    print("To add items to the list type \"add\"")
    print("To edit your list type \"edit\"")
    print("To quit type \"exit\"")
    user_choice=input("> ")
    
    if user_choice.lower() == "edit":
        os.system("cls")
        print("1.) Change Name of item in list")
        print("2.) remove item from list")
        print("3.) clear list")
        edit_choice = input("> ")
        
        if edit_choice == "1":
            item_to_edit = input("Which item would you like to edit?\n> ")
            try:
                edit_this = my_list.index(item_to_edit)
                my_list[edit_this] = input("What is the new name of the item?\n> ")
            except ValueError:
                print("Error Invalid Item name")
            time.sleep(1.5)
            os.system("cls")
        elif edit_choice == "2":
            try:
                to_remove = input("Which item do you want to remove?\n")
                choice = input(f"Are you sure you want to remove \33[31m{to_remove}\33[0m\n")
                if choice.lower() in ["yes","y","ja"]:
                    my_list.remove(to_remove)
                    print(f"You have removed {to_remove}")
                time.sleep(1)
                os.system("cls")
            except ValueError:
                print("The item you have choosen is not in the list!")
                time.sleep(1.5)
                os.system("cls")
        elif edit_choice == "3":
            my_list.clear()
            print("List has been cleared")
            time.sleep(1)
            os.system("cls")
        else:
            print("Invalid Choice")
            time.sleep(1)
            os.system("cls")
                
    elif user_choice.lower() == "add":
        os.system("cls")
        item_to_add = input("What do you want to add to your todo list?\n> ")
        if item_to_add not in my_list:
            my_list.append(item_to_add)
            print(f"Added {item_to_add} to list")
            time.sleep(1)
        else:
            os.system("cls")
            print("Item not added Item already in list")
            time.sleep(1.5)
        
        os.system("cls")
        
    elif user_choice.lower() == "view":
        os.system("cls")
        if len(my_list) == 0:
            print("List is empty")
            
        else:
            printlist()
        time.sleep(1.5)
        
    elif user_choice.lower() in ["exit","quit","leave","bye"]:
        break
    
    else:
        print("Invalid command")
        
    