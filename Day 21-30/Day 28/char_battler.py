import os
import time
import random

# Funktion zum Lesen von Zeilen aus einer Datei
def read_lines_from_file(file_path):
    with open(file_path, "r",encoding="utf-8") as file:
        lines = file.readlines()
    return lines

# Funktion zum Zufällige Element aus einer Liste auswählen
def get_random_element(lines):
    random_index = random.randint(0, len(lines) - 1)
    return lines[random_index].strip()

# Funktion zum Generieren eines Charakternamens
def name_gen():
    first_names = read_lines_from_file("D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 21-30\\Day 27\\first-names.txt")
    titles = read_lines_from_file("D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 21-30\\Day 27\\title_list.txt")

    # Benutzereingabe für benutzerdefinierten Namen
    custom_name = input("\nPlease enter a custom name or leave this blank for a random name: ").strip()

    # Zufälliger Name und Titel auswählen
    if not custom_name:
        random_name = get_random_element(first_names)
        random_title = get_random_element(titles)
        return f"\033[34m{random_name} {random_title}\033[0m"
    else:
        # Benutzerdefinierter Name mit großgeschriebenem Anfangsbuchstaben
        return f"\033[34m{custom_name.capitalize()} {get_random_element(titles)}\033[0m"

# Funktion zum Auswahl einer Rasse
def race_picker():
    races_file = read_lines_from_file("D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 21-30\\Day 27\\races.txt")

    # Benutzereingabe für benutzerdefinierte Rasse
    custom_race = input("\nPlease enter a custom race or leave this blank for a random race: ").strip()

    # Zufällige Rasse auswählen
    if not custom_race:
        return f"\033[33m{get_random_element(races_file)}\033[0m"
    else:
        # Benutzerdefinierte Rasse mit großgeschriebenem Anfangsbuchstaben
        return f"\033[33m{custom_race.capitalize()}\033[0m"

# Funktion zum Würfeln eines n-seitigen Würfels
def sided_die(sides):
    result = random.randint(1, sides)
    return result

# Funktion zum Generieren von Gesundheitswerten
def generate_stat(stat_name):
    stat = (sided_die(6) * sided_die(12)) / 2 + (12 if stat_name == "strength" else 10)
    return stat

char1_name = name_gen()
char1_race = race_picker()
char1_strength= generate_stat("strength")
char1_health = generate_stat("health")

char2_pick_name = name_gen()
char2_name = f"{char2_pick_name}"
char2_race = race_picker()
char2_strength= generate_stat("strength")
char2_health = generate_stat("health")



def winner():
    char1 = sided_die(6)
    char2 = sided_die(6)
    if char1 > char2:
        return "one"
    elif char2 > char1:
        return "two"
    elif char1 == char2:
        return "draw"
    
os.system("cls")
count = 0
while True:
    damage1 = abs(char1_strength - (char2_strength/2+1))
    damage2 = abs(char2_strength-(char1_strength/2+1))  
    print("Battle Time!")
    
    print(f"\nName: {char1_name}\nRace: {char1_race}\nStrength: {char1_strength}\nHealth: {char1_health}")
    print("\nvs\n")
    print(f"\nName: {char2_name}\nRace: {char2_race}\nStrength: {char2_strength}\nHealth: {char2_health}")
    time.sleep(3)
    os.system("cls")
    while True:
        first = winner()
        print(f"\nName: {char1_name}\nRace: {char1_race}\nStrength: {char1_strength}\nHealth: {char1_health}")
        print("\nvs\n")
        print(f"\nName: {char2_name}\nRace: {char2_race}\nStrength: {char2_strength}\nHealth: {char2_health}")

        if first == "one":
            char2_health -= damage1
            if count == 0:
                print(f"{char1_name} gets the first blow, {char2_name} takes {damage1} damage")
            else:
                print(f"{char1_name} wins round {count}, {char2_name} takes {damage1} damage")
        elif first == "two":
            char1_health -= damage2
            if count == 0:
                print(f"{char2_name} gets the first blow, {char1_name} takes {damage2} damage")
            else:
                print(f"{char2_name} wins round {count}, {char1_name} takes {damage2} damage")
                
        time.sleep(3)
        os.system("cls")
        if char1_health <= 0:
            print(f"Oh no {char1_name} died in {count} rounds.\nThat makes {char2_name} the winner.")
            break
        elif char2_health <= 0:
            print(f"Oh no {char2_name} died in {count} rounds.\nThat makes {char1_name} the winner.")
            break
        count += 1
    break

