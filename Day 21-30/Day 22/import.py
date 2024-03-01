#Code von Tag 18 da ich die challenge schon an tag 18 gelöst habe


import random

while True:
    number = int(random.randint(1,1000000))
    tries = 0

    print("Welcome to the random number guesser.\nGuess the a number between 1 and 1.000.000 :)\n")
    while True:
        try:
            guess = int(input("Please enter your guess: "))
            tries += 1
            if guess > number:
                print(f"Your guess of {guess} is too high")
            elif guess < number:
                print(f"Your guess of {guess} is too low")
            elif guess == number and tries < 20:
                print(f"You did it :) you guessed the number {number} right and it only took you {tries} tries.")
                break
            elif guess == number and tries > 20:
                print(f"Finally you guessed the number {number}. Maybe next time don't take {tries} tries")
                break
        except ValueError:
            print("please enter a valid number")
    
    choice = input("\n1.) Go again\n2.) exit\n")
    while True:
        if choice == "1":
            print("Going again")
            break
        elif choice == "2":
            print("See you next time :)")
            exit()
        else:
            print("Invalid Choice. Plese enter 1 or 2.")
    
