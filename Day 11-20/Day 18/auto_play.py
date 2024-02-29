import subprocess

def auto_play():
    while True:
        # Starte das Spiel als Subprozess
        process = subprocess.Popen(["python", "D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 11-20\\Day 18\\number_guess.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        # Initialisiere die Grenzen des Zahlenbereichs
        low_limit, high_limit = 1, 1000000
        # Zähle die Versuche
        tries = 0

        # Äußere Schleife: Spiel wird wiederholt, bis der Benutzer entscheidet zu beenden
        while low_limit <= high_limit:  # Änderung: Schleife bis die Optionen erschöpft sind
            # Rate die Mitte des aktuellen Zahlenbereichs
            guess = (low_limit + high_limit) // 2

            # Gib aus, welche Zahl gerade geraten wird
            print(f"Guessing {guess}...")

            # Erhöhe die Anzahl der Versuche
            tries += 1

            # Versuche, die geratene Zahl an das Spiel zu senden und die Antwort zu lesen
            try:
                # Schreibe die geratene Zahl in den Prozess
                process.stdin.write(str(guess) + "\n")
                process.stdin.flush()
                # Lese die Ausgabe des Spiels
                output = process.stdout.readline()

                # Überprüfe die Ausgabe, um den Fortschritt zu bestimmen
                if "right" in output or "Finally" in output:
                    # Der Auto-Spieler hat die Zahl richtig geraten
                    print(f"Auto player guessed the number {guess} right in {tries} tries.")
                    print(f"The number was {guess}.")  # Hinzugefügtes Print-Statement
                    break
                elif "high" in output:
                    # Die geratene Zahl ist zu hoch
                    print("Too high!")
                    high_limit = guess - 1
                elif "low" in output:
                    # Die geratene Zahl ist zu niedrig
                    print("Too low!")
                    low_limit = guess + 1
                # Gib den angepassten Zahlenbereich aus
                print(f"Adjusted range: {low_limit} - {high_limit}")
            except ValueError:
                # Fehler bei der Kommunikation mit dem Spiel
                print("Error communicating with the game.")
                break  # Beende die innere Schleife im Fehlerfall

        # Gib die geratene Zahl erneut aus
        print(f"\nThe number was {guess} it took {tries} tries")
        # Frage den Benutzer, ob er erneut spielen oder beenden möchte
        choice = input("\n1.) Go again\n2.) Exit\n")

        # Überprüfe die Benutzerwahl
        if choice != "1":
            # Der Benutzer möchte nicht erneut spielen
            print("See you next time :)")
            break

# Hauptprogramm: Starte das Spiel, wenn dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    auto_play()
