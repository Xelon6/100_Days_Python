import os
import time
import random

os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Initialisierung von Variablen für falsch geratene Buchstaben und bereits geratene Buchstaben
wrong_letter = ""
guessed = ""

# Öffnen der Wortliste aus einer Datei
with open("wordlist.txt", "r", encoding="utf8") as wordlist:
    # Erstellen einer Liste von Wörtern aus der Wortliste
    words = [word.strip() for word in wordlist.readlines()]

# Zufällige Auswahl eines Wortes aus der Liste und Umwandlung in Kleinbuchstaben
random_word = random.choice(words).lower()

# Erstellung einer Zeichenkette zur Anzeige der Buchstaben im Spiel
display_ = len(random_word) * "_ "

# Funktion zum Aktualisieren der Anzeige des geratenen Wortes
def update_display(word, display, letter, guessed_letters):
    updated_display = ""
    
    for i, char in enumerate(word):
        if char == letter:
            updated_display += letter + " "
            guessed_letters += letter
        else:
            updated_display += display[i * 2] + " "

    return updated_display.strip(), guessed_letters

# Funktion zum Löschen der Konsole (für einen klareren Bildschirm)
def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

# Funktion für falsch geratene Buchstaben
def wrong_letters(word, letter, wrong, lives_max, right_letters):
    if letter not in word:
        if letter not in wrong:
            wrong += letter
            lives_max -= 1
    elif letter in word:
        if letter not in right_letters:
            right_letters += letter
    return wrong, lives_max, right_letters

# Spielbeginn
print("Lets play Hangman")
print(display_)

lives = 6
while True:
    
    # Benutzereingabe für einen Buchstaben
    guess = input("\nGuess a letter\n>")
    clear_console()
    if len(guess) > 1:
        print("Please only enter 1 letter at a time")
        continue
    
    # Überprüfung auf falsch geratene Buchstaben und Aktualisierung der Anzeige
    wrong_letter, lives, right_letter = wrong_letters(random_word, guess, wrong_letter, lives, guessed)
    display_, guessed = update_display(random_word, display_, guess, guessed)
    
    print()
    print(display_)
    print()
    print(f"Wrong Letters: {wrong_letter}")

    # Überprüfung auf Spielende (keine Leben mehr oder alle Buchstaben geraten)
    if lives == 0:
        print(f"You have 0 Lives left. You lost. The word was\n{random_word}")
        break
    elif set(guessed) == set(random_word):
        clear_console()
        print(f"Your guess was right. The word was {random_word}")
        time.sleep(2)
        break
    else:
        print(f"You have {lives} lives left")
        print("-----------------------------------")
