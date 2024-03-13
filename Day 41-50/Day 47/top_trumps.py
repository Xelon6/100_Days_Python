import os
import random
import time



trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Strength": 80, "Endurance": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Strength": 50, "Endurance": 0}
trumps["Megamind"] = {"Intelligence": 300, "Speed": 5, "Strength": 5, "Endurance": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Strength": 200, "Endurance": 101}

def clear_console():
    """Clear console"""
    os.system('clear' if os.name == 'posix' else 'cls')

def add():
    """add characters"""
    clear_console()
    name = input("What is your new Trumps Name?\n> ")
    print("Now for it Stats")
    while True:
        try:
            intelligence = int(input("How high is your Trumps Intelligence?\n> "))
            print()
            speed = int(input("How high is your Trumps Speed?\n> "))
            print()
            strength = int(input("How high is your Trumps Strength?\n> "))
            print()
            end = int(input("How high is your Trumps Endurance?\n> "))
            break
        except ValueError:
            clear_console()
            print("Please enter a whole number")
            time.sleep(1)
            clear_console()
            continue

    trumps[name] = {"Intelligence": intelligence,
                    "Speed": speed,
                    "Strength": strength,
                    "Endurance": end}
    clear_console()
    print("You have succesfully created:")
    print(f"\33[36m{name}\33[0m with the Stats of:")
    print()
    for key,value in trumps[name].items():
        print(f"{key:<15}:\33[36m{value}\33[0m")
    input("Enter a key to go back to the menu...")


def menu():
    """printet alle menu optionen"""
    print()
    print("What do you want to do?")
    print("1.) Battle")
    print("2.) View Trumps")
    print("3.) Add Trumps")
    print("4.) Exit")

def battle():
    """Battle mechanic"""
    clear_console()
    print("Choose your Trump:")
    while True:
        for key in trumps.keys():
            print(f"{key} ",end=("| "))
        user = input("\n> ").strip()
        comp =random.choice(list(trumps.keys()))
        print()
        print(f"You have choosen {user}")
        print()
        if user in trumps:
            break
        clear_console()
        print("Invalid Trump chosen")
        time.sleep(1)
        
    print(f"The Computer has choose {comp}")
    print()
    print("Choose your stat:\n1.) Intelligence\n2.) Speed\n3.) Strength\n4.) Endurance")
    stat = input("> ").lower().strip()
    if "int" in stat or stat == "1":
        stat = "Intelligence"
    elif "spe" in stat or stat == "2":
        stat = "Speed"
    elif "str" in stat or stat =="3":
        stat="Strength"
    elif "end" in stat or stat == "4":
        stat = "Endurance"
    else:
        print("Invalid stat choosen")

    if trumps[user][stat] < trumps[comp][stat]:
        print("The Computer's Trump",comp,"has Won.")
    elif trumps[user][stat] > trumps[comp][stat]:
        print("Your Trump",user,"has Won. :)")
    else:
        print("Draw")


def view():
    """zeigt alle chars"""
    for keys,values in trumps.items():
        print()
        print(f"\33[36m{keys}\33[0m Has the following Stats")
        for stat_name,stats in values.items():
            print(f"{stat_name:<15}:\33[36m{stats}\33[0m")
    print()


def main():
    """main funktion"""
    while True:
        clear_console()
        print("Top Trumps")
        menu()
        choice = input("> ").lower().strip()

        #check was der user machen will
        if choice in ["1", "battle"]:
            clear_console()
            battle()
            print()
            input("Enter any key to go back to the menu...")
            clear_console()
        elif choice in ["2","view"]:
            clear_console()
            view()
            input("Enter any key to go back to the menu...")
            clear_console()
        elif choice in ["3","add"]:
            clear_console()
            add()
            clear_console()
        elif choice in ["4","quit","exit","bye"]:
            clear_console()
            print("Till next Time :)")
            time.sleep(1)
            exit()



if __name__ == "__main__":
    main()
