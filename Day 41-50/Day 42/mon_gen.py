types = {
    "1":"earth",
    "2":"fire",
    "3":"water",
    "4":"air",
    "5":"spirit"
}

monster = {
    "Monster Name":None,
    "Type":None,
    "Special Move":None,
    "HP":None,
    "MP":None
}


def get_type():
    print("Choose one of the following types:")
    for key,value in types.items():
        print(f"{key}:{value.capitalize()}")
    choosen = input("Enter the number or name of the type you want\n>").strip()
    if len(choosen) > 1:
        return choosen.title()
    else:
        choosen = types[choosen]
        return choosen.title()
        

def get_input():
    
    for arg in monster.keys():
        if arg == "Type":
            monster[arg] = get_type()
        elif arg in {"HP","MP"}:
            while True:
                try:
                    monster[arg] = int(input(f"Input your beast's {arg}\n>").strip())
                    if monster[arg] >= 0:
                        break
                    else:
                        print(f"Please enter a non-negative number for {arg}")
                except ValueError:
                    print(f"Please enter a valid number for {arg}")
        else:
            monster[arg] = input(f"Input your beast's {arg}\n>").strip().title()
    print()

def color_text(mon_type):
    color_codes = {
        types["1"]: "\33[32m",
        types["2"]: "\33[31m",
        types["3"]: "\33[34m",
        types["4"]: "\33[37m",
        types["5"]: "\33[35m",
    }
    return color_codes.get(mon_type, "\33[0m")

def main():
    get_input()
    mon_type = monster["Type"].lower()
    print(color_text(mon_type),"Your Monsters stats are:")
    for keys,value in monster.items():
        print(f"{color_text(mon_type)}{keys:<15}: {value}")
    print("\33[0m")
    

if __name__ == "__main__":
    main()