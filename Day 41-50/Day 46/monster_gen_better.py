import os

types = {
    "1":"earth",
    "2":"fire",
    "3":"water",
    "4":"air",
    "5":"spirit"
}
monsters = {}

def clear_console():
    """Clear console"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_type():
    """Type von monster auswählen """
    print("Choose one of the following types:")
    for key,value in types.items():
        print(f"{key}:{value.capitalize()}")
    choosen = input("Enter the number or name of the type you want\n> ").strip()
    if len(choosen) > 1:
        return choosen.title()
    else:
        choosen = types[choosen]
        return choosen.title()


def get_input():
    """input von user zum monster erstellen """
    monster = {
    "Name":None,
    "Type":None,
    "Special Move":None,
    "HP":None,
    "MP":None
    }

    for arg in monster.keys():
        if arg == "Type":
            monster[arg] = get_type()
        elif arg in {"HP","MP"}:
            while True:
                try:
                    monster[arg] = int(input(f"Input your beast's {arg}\n> ").strip())
                    if monster[arg] >= 0:
                        break
                    else:
                        print(f"Please enter a non-negative number for {arg}")
                except ValueError:
                    print(f"Please enter a valid number for {arg}")
        else:
            monster[arg] = input(f"Input your beast's {arg}\n> ").strip().title()

    return monster["Name"],monster["Type"],monster["Special Move"],monster["HP"],monster["MP"]



def color_text(mon_type):
    """Text Farbe hinzufügen"""
    color_codes = {
        types["1"]: "\33[32m",
        types["2"]: "\33[31m",
        types["3"]: "\33[34m",
        types["4"]: "\33[37m",
        types["5"]: "\33[35m",
    }
    return color_codes.get(mon_type.lower(), "\33[0m")


def view():
    """Monsters anzeigen"""
    for key, value in monsters.items():
        mon_type= value["Type"]
        print(f"\n\033[1m {color_text(mon_type)}{key}\33[0m Has the Following Stats")
        for subkey, subvalue in value.items():
            print(f"{subkey:<15}: \033[1m {color_text(mon_type)} {subvalue}\33[0m")
    print("\33[0m")


def main():
    """main"""
    while True:
        clear_console()
        monster_name, monster_type,monster_move,monster_hp,monster_mp = get_input()
        monsters[monster_name] = {"Type":monster_type,
                                  "Special Move":monster_move,
                                  "HP":monster_hp,
                                  "MP":monster_mp}
        clear_console()
        print("Do you want to\n1.) View Monsters\n2.) Create another\n3.) Exit")
        choice = input("> ").lower().strip()
        clear_console()
        if choice in ["1", "view","show"]:

            view()
            input("Enter a key to create another one...  ")
            clear_console()
        elif choice in ["2","create","another"]:
            continue
        elif choice in ["exit","quit","3"]:
            exit()
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
