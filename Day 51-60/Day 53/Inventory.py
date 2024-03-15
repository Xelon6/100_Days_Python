import os
import time
import json

# Change the current directory to the directory of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def clear_console():
    """Clears the console window."""
    os.system('clear' if os.name == 'posix' else 'cls')

# File name to store inventory data
FILE_NAME = "inventory.list"
inventory = []

# Clear the console at the beginning
clear_console()

# Attempt to load existing inventory data from file, create a new inventory if the file doesn't exist
try:
    with open(FILE_NAME, "r", encoding="UTF-8") as file:
        inventory = json.load(file)
except FileNotFoundError:
    print("No existing file. Starting with a blank inventory.")
    time.sleep(1.5)
    clear_console()

def save_to_file():
    """Saves the inventory data to a file."""
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        json.dump(inventory, f)

def menu():
    """Displays the menu and returns the user's choice."""
    print()
    print("Inventory manager:")
    print("1.) Add Item to Inventory")
    print("2.) Remove Item from Inventory")
    print("3.) View Items in Inventory")
    print("4.) Exit")
    x = input("> ").lower().strip()
    return x

def add():
    """Adds items to the inventory."""
    clear_console()
    print("Input the name of the item you want to add:")
    item = input("> ").strip().capitalize()
    while True:
        print("How many times do you want to add it?")
        try:
            qty = int(input("> "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    inventory.extend([item] * qty)
    print(f"Added {item} {qty} times to your inventory.")
    time.sleep(1)
    clear_console()

def view_all():
    """Displays all items in the inventory along with their quantities."""
    clear_console()
    view_list = []
    max_item_length = max(len(item) for item in inventory)  # Find the length of the longest item name
    for item in inventory:
        if item not in view_list:
            count = inventory.count(item)
            print(f"{item:<{max_item_length}} {count:>15}")
            view_list.append(item)
    input("\nPress any key to go back to the menu...")
    clear_console()

def remove():
    """Removes items from the inventory."""
    clear_console()
    print("Which item would you like to remove?")
    x = input("> ").strip().lower()
    for item in inventory:
        if item.lower() == x:
            inventory.remove(item)
            print(f"Removed {item} once from the inventory.")
            time.sleep(1.5)
            clear_console()
            break
    else:
        print(f"Couldn't remove {x}. Please check your spelling.")
        time.sleep(2)
        clear_console()

def main():
    """Main function to run the inventory management system."""
    while True:
        choice = menu()
        if choice in ["1", "add"]:
            add()
        elif choice in ["2", "remove", "delete"]:
            remove()
        elif choice in ["3", "view", "list"]:
            view_all()
        elif choice in ["4", "exit"]:
            clear_console()
            print("See you next time!")
            save_to_file()  # Save inventory data before exiting
            time.sleep(1.5)
            exit()
        else:
            clear_console()
            print("Invalid choice.")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()
