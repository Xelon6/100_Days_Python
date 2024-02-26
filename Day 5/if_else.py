character_choosen = False
while character_choosen != True:
    print("Choose your character")
    print("1.) Warrior")
    print("2.) Mage")
    print("3.) Rogue")
    print("4.) Archer")
    print("5.) to quit")
    choice = input("Enter the number of your Character of choice:  ")
    if choice == "1":
        print("You choose Warrior:\nAh you like fighting up close and personal")
        character_choosen = True
    elif choice == "2":
        print("You choose Mage:\nYou are not that smart i know that")
        character_choosen = True
    elif choice == "3":
        print("You choose Rogue:\nTrying to be stealhty with your weight?")
        character_choosen = True
    elif choice == "4":
        print("Archer:\nI know that your aim is bad")
        character_choosen = True
    elif choice == "5":
        print("you quit :(")
        break
    else:
        print("please choose a valid character")
