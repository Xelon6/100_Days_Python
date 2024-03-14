import os
import time
import json

os.chdir(os.path.dirname(os.path.realpath(__file__)))

def clear_console():
    """cleared console auf win und unix"""
    os.system('clear' if os.name == 'posix' else 'cls')


def clear_wait():
    """cleared console auf win und unix und wartet"""
    time.sleep(2)
    os.system('clear' if os.name == 'posix' else 'cls')

# starte leere liste
pizzas = []

try:
    with open("pizza.orders", "r", encoding="UTF-8") as file:
        pizzas = json.load(file)
except FileNotFoundError:
    print("No existing File starting with a blank one")
    clear_wait()
    # Handle the case when the file does not exist

def toppings():
    """toppings select"""
    pizza_toppings = ['Pepperoni', 'Mushrooms', 'Ham', 'Pineapple', 'Olives', 'Bell peppers', 'Onions', 'Spinach', 'Garlic', 'Anchovies', 'Tomatoes', 'Artichokes', 'Broccoli', 'Sausage', 'Arugula', 'Chilies', 'Corn', 'Capers']
    print("Please choose one or more of the following toppings:")
    
    # Print out all available toppings
    for topping in pizza_toppings:
        print(topping, end=", ")
    
    chosen = []  # List to store the chosen toppings
    
    while True:
        choice = input("\n> ").strip()
        if choice == "":
            break  # If the user enters nothing, exit the loop
        chosen.append(choice)
        add_another = input("Do you want to add another topping? (y/n)\n> ")
        if add_another.lower() != "y":
            break
    
    # Check if any toppings were chosen
    if chosen:
        print("Your chosen toppings are:")
        for x in chosen:
            print(x, end=", ")
        price = len(chosen) * 0.40  # Calculate price based on the number of chosen toppings
        print(f"\nThe price of your toppings is {price:.2f}€")
        return price
    else:
        print("No toppings selected.")

def size_chooser():
    while True:
        print("Please choose a size.\nS/M/L/XL\n")
        size_ = input("> ").strip().lower()
        if size_ in ["s", "m", "l", "xl"]:
            if size_ == "s":
                cost = 6.99
            elif size_ == "m":
                cost = 8.99
            elif size_ == "l":
                cost = 10.99
            elif size_ == "xl":
                cost = 13.99
            return cost,size_.upper()
        else:
            print("Please choose a valid size")



def add():
    '''Funktion um pizzen zu adden'''
    clear_console()
    name = input("What is your Name?\n> ")
    cost,size = size_chooser()
    cost_toppings = toppings()
    while True:
        try:
            qty = int(input("How many pizzas would you like?\n> "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        break
    if cost_toppings:
        price = cost * qty + cost_toppings
    else:
        price = cost * qty
    order_number = len(pizzas) +1
    order = [order_number,name,price,size,qty]
    pizzas.append(order)
    if qty > 1:
        print(f"Thank you {name}, your {qty} pizzas will cost {price:.2f}€")
    else:
        print(f"Thank you {name}, your {qty} pizza will cost {price:.2f}€")

def save_to_file():
    '''save to file'''
    with open("pizza.orders","w",encoding="UTF-8") as f:
        json.dump(pizzas,f)

def view():
    '''view all orders'''
    print("You have the following orders:\n")
    for order in pizzas:
        print(f"Order Number: {order[0]} | Name: {order[1]} | Price: {order[2]}€ | Size: {order[3]} | Quantity: {order[4]}")

def remove_order():
    '''remove a order'''
    print("Which order would you like to remove")
    view()
    x = input("\n> ")
    for order in pizzas:
        if x in order:
            pizzas.remove(order)
            print(f"Removed {order}")
            break
    else:
        print("Couldn't find the order :(")



def main():
    while True:
        clear_console()
        x = input("Do you want to\n1.) Place a order\n2.) View orders\n3.) Remove order\n4.) Exit\n> ").lower().strip()
        if x in ["1","place","add"]:
            add()
            clear_wait()
        elif x in ["2","view"]:
            clear_console()
            view()
            input("Enter a Key to go back to the menu...")
            clear_console()
        elif x in ["3","remove"]:
            clear_console()
            remove_order()
            clear_wait()
        elif x in ["4","exit","quit"]:
            clear_console()
            print("Goodbye :)")
            clear_wait()
            save_to_file()
            exit()


if __name__ == "__main__":
    main()