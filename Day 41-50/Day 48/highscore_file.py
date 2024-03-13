
print("🌟HIGH SCORE TABLE🌟")


while True:

    print()
    initials = input("Input your Initials > ").strip().upper()
    score = input("Input your score > ").strip()
    f = open("D:\\Cybersec\\Python\\100 Days Python\\100_Days_Python\\Day 41-50\\Day 48\\high.score","a+",encoding="UTF-8")
    f.write(f"{initials} {score}\n")
    f.close()
    choice= input("Add another one? y/n? ").lower().strip()
    if choice == "n":
        break
