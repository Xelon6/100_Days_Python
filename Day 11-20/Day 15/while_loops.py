while True:
    animal = input("What animal sound do you want to hear?: ")

    # Convert the user input to lowercase for case-insensitive comparison
    animal_lower = animal.lower()

    # Define the animal sounds
    animal_sounds = {
        'cow': 'A cow goes moo.',
        'lesser spotted lemur': 'Ummm...the Lesser Spotter Lemur goes awooga.',
        'cat': 'A cat says meow.',
        'dog': 'A dog barks.',
        'elephant': 'An elephant trumpets.',
        'frog': 'A frog says ribbit.',
        'lion': 'A lion roars.',
        'monkey': 'A monkey chatters.',
        'owl': 'An owl hoots.',
        'penguin': 'A penguin makes a honking sound.'
        # Add more animals and their sounds as needed
    }

    # Check if the entered animal is in the dictionary
    if animal_lower in animal_sounds:
        print(animal_sounds[animal_lower])
    else:
        print("Sorry, I don't know the sound of that animal.")

    exit_choice = input("Do you want to exit? (yes/no): ").lower()

    if exit_choice in ['yes','y','ja']:
        break  # Exit the loop if the user wants to exit
