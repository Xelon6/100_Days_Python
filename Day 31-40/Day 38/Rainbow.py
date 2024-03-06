
sentence = input("Please enter a sentence to rainbowfiy\n> ")

for letter in sentence:
    if letter.lower() == "r":
        print("\33[31m",end='')
    elif letter.lower() == "b":
        print("\33[34m",end='')
    elif letter.lower() == "y":
        print("\33[33m",end='')
    elif letter.lower() == "g":
        print("\33[32m",end='')
    elif letter.lower() == "p":
        print("\33[35m",end='')
    elif letter == " ":
        print("\33[0m",end='')
    print(letter,end="")
