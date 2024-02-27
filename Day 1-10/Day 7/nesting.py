def fan_question_generator():
    print("Welcome to the Fake Fan Question Generator!")

    interest = input("What are you interested in? ")

    if interest.lower() == "the big bang theory":
        print("Great choice! Let's see if you're a true fan.")

        lead_actor = input("Who is the lead actor in The Big Bang Theory? ")

        if lead_actor.lower() == "jim parsons":
            print("Correct! Now, how many seasons does the show have?")
            
            big_bang_seasons = int(input("Enter the number of seasons: "))

            if big_bang_seasons == 12:
                print("Well done! You seem to be a true fan of The Big Bang Theory.")
            else:
                print("Oops! The Big Bang Theory actually has 12 seasons. Try again!")
        elif lead_actor.lower() == "johnny galecki":
            print("Close, but Johnny Galecki plays Leonard Hofstadter. Try again!")
        else:
            print("Wrong actor! Jim Parsons plays Sheldon Cooper in The Big Bang Theory.")
    else:
        print("Sorry, this program is designed for The Big Bang Theory fans only. Please try another interest.")

# Run the Fake Fan Question Generator
fan_question_generator()
