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

print("Welcome to the Character Creator")
time.sleep(2)

while True:
    os.system("cls")

    # Charakterinformationen generieren
    name = name_gen()
    race = race_picker()
    health = generate_stat("health")
    strength = generate_stat("strength")

    os.system("cls")

    # Charakterinformationen ausgeben
    print(f"Your Character's Name is:\n{name}\n")
    print(f"\nCharacter Race:\n{race}\n")
    print(f"\nHealth: {health}\nStrength: {strength}")
    print("May your name go down in Legend ...")

    time.sleep(2)

    # Benutzerabfrage für die Generierung eines weiteren Charakters
    choice = input("\n\nDo you want to generate another one? Y/N: ")

    if choice.lower() in ["yes", "y"]:
        continue
    else:
        break
