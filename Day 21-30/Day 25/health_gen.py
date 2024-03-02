import random

def roll_die(sides):
    die = int(random.randint(1,sides))
    return die

def health_gen():
    health = roll_die(6) * roll_die(8)
    return health

count=0
while True:
    char_name=input("Whats the name of your character?: ")
    char_name_color = f"\033[34m{char_name}\033[0m"
    print(f"Character name: {char_name_color}\n Health Points: \33[31m{health_gen()}\33[0m")
    count +=1
    another = input("Do you want to generate another character?\nY/N  ")
    if another.lower() in ["n","no", "exit", "quit"]:
        if count > 1:
            print("I wish your warriors the best")
        else:
            print("I wish",char_name_color,"a successful fight.")

        break
    else:
        continue

