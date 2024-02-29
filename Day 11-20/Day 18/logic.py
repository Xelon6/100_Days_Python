import random

def auto_play():
    while True:
        number = random.randint(1, 1000000)
        low_limit, high_limit = 1, 1000000
        tries = 0

        print("Welcome to the random number guesser.\nGuess the number between 1 and 1,000,000.\n")

        while True:
            # Adaptive Ratenstrategie: Berechne die Mitte des aktuellen Intervalls
            guess = (low_limit + high_limit) // 2

            print(f"Guessing {guess}...")

            tries += 1

            # Überprüfe, ob die geratene Zahl korrekt ist
            if guess == number:
                if tries < 20:
                    print(f"You guessed {guess} right in {tries} tries! Well done.")
                else:
                    print(f"Finally, you guessed {guess} in {tries} tries. Next time, aim for fewer tries!")
                break

            # Passe das Intervall basierend auf dem Feedback an
            elif guess > number:
                print("Too high! Adjusting the range...")
                high_limit = guess - 1
            else:
                print("Too low! Adjusting the range...")
                low_limit = guess + 1

        choice = input("\n1.) Go again\n2.) Exit\n")

        if choice != "1":
            print("See you next time :)")
            break

auto_play()
