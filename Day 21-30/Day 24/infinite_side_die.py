
sides= int(input("How many sides ? "))
def roll_die(sites):
    import random
    die = int(random.randint(1,sites))
    return f"You rolled your {sites} sided die and got {die}"

again  =""
while again.lower() not in ["no","n", "exit", "quit"] :

    print(roll_die(sides))

    again=input("Roll again? yes/no: ")

