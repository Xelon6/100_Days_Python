counter = 0

while True:
    print("Fill in the missing word in the lyrics\n")
    guess = input("Never going to ______ you up.\n")
    if guess.lower() != "give":
        counter += 1
        print(guess,"is wrong")
    else:
        print("Never going to give you up.\nIs right Gongratulations it only took you",counter,"tries.")
        break