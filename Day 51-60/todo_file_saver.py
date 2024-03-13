import os
import time
import json

os.chdir(os.path.dirname(os.path.realpath(__file__)))




try:
    with open("todo.list", "r", encoding="UTF-8") as file:
        todo_list = json.load(file)
except FileNotFoundError:
    # Handle the case when the file does not exist
    todo_list = [["High Priority",[]],
             ["Medium Priority",[]],
             ["Low Priority",[]]]



def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def menu():
    clear_console()
    print("Welcome to your todo list")
    print("What would you like todo :)?")
    print("1.) add Task\n2.) view Tasks\n3.) edit List/Task\n4.) save Tasks to file\n5.) Exit")
    choice = input("> ").strip()
    try:
        if choice.lower() in ["add","1"]:
            choice = 1
        elif choice.lower() in ["view","2"]:
            choice = 2
        elif choice.lower() in ["edit","3"]:
            choice = 3
        elif choice.lower() in ["save","4"]:
            choice = 4
        elif choice.lower() in ["exit","quit","5","bye"]:
            clear_console()
            print("See you next Time :)")
            time.sleep(1)
            clear_console()
            exit()
        else:
            print("Please choose a valid option")
    except ValueError:
        print("Please use a valid input")
    return choice

def print_all():
    for row in todo_list:
        print()
        print(row[0])
        print()
        for item in row[1]:
            print(f"Todo: {item[0]}\t{item[1]}")


def view():
    clear_console()
    choice = input("1.) View all\n2.) View Priority\n> ").lower().strip()
    
    if choice in ["1","all","view all"]:
        clear_console()
        print_all()
        input("Press any Key to go back to the menu: ")

    elif choice in ["2","priority","view priority"]:
        clear_console()
        print("Which Priority do you wanna see the Tasks of?")
        print(f"{todo_list[0][0]}\n{todo_list[1][0]}\n{todo_list[2][0]}")
        priority_choice = input("> ").lower().strip()
        clear_console()
        for row in todo_list:
            if priority_choice.capitalize() in row[0]:
                print(row[0])
                print()
                for item in row[1]:
                    print(f"Todo: {item[0]}\t{item[1]}")
        input("Press any Key to go back to the menu: ")
    else:
        clear_console()
        print("Please enter a valid Choice")
        time.sleep(1)




def add():
    clear_console()
    todo = input("What is the Task?\n> ").title().strip()
    due = input("When do you need to do it ?\n> ").strip().capitalize()
    priority = input("How important is it ?\nHigh Priority\nMedium Priority\nLow Priority\n> ").lower().strip()
    
    new_Task = [todo,due]
    
    for row in todo_list:
        if priority.capitalize() in row[0]:
            row[1].append(new_Task)
            break
    else:
        clear_console()
        print("Invalid Priority Task not added")
        time.sleep(1.5)
    clear_console()


def edit():
    clear_console()
    print("1.) Edit Task\n2.) Remove Task")
    choice = input("> ").lower().strip()
    
    if choice in ["edit", "1"]:
        clear_console()
        print_all()
        to_edit = input("Which Task do you want to edit?\n> ")
        new_task = input("What is the new task?: ")
        new_due = input("When is it due?: ")
        
        for row in todo_list:
            for item in row[1]:
                if to_edit in item:
                    item[0] = new_task
                    item[1] = new_due
                    break
                else:
                    print("couldn't find the task :(")
        
    elif choice in ["remove","2"]:
        clear_console()
        print_all()
        find = input("Name of Task to remove\n> ")
        

        to_remove = []

        for row in todo_list:
            for item in row[1]:
                if find in item:
                    to_remove.append(item)

        for item in to_remove:
            for row in todo_list:
                if item in row[1]:
                    row[1].remove(item)
                    break
    else:
        clear_console()
        print("Please enter a valid Choice")
        time.sleep(1)


def save_to_file():
    try:
        with open("todo.list","w",encoding=("UTF-8")) as f:
            json.dump(todo_list,f)
        print("Saved Task successfully :)")
    except PermissionError as e:
        print(f"Error saving data {e}")
    except FileNotFoundError as e:
        print(f"Error saving data {e}")
    except Exception as e:#pylint: disable=broad-exception-caught
        print(f"Error saving data {e}")
    


while True:
    choosen = menu()
    
    if choosen == 1:
        clear_console()
        add()
        clear_console()
        
    elif choosen == 2:
        view()        
    elif choosen == 3:
        clear_console()
        edit()
        clear_console()
    elif choosen == 4:
        clear_console()
        save_to_file()
        time.sleep(1)
        clear_console()
    else:
        print("Please enter a valid option")

