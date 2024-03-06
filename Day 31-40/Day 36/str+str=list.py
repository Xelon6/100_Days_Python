
names = []

def printlist():
    print()
    for i in names:
        print(i)
    print()

while True:
    first_name = input("First name: ").strip().capitalize()
    last_name = input("Last Name: ").strip().capitalize()
    full_name = f"{last_name} {first_name}"
    if full_name not in names:
        names.append(full_name)
        printlist()
    else:
        print("\nDuplicate")
        printlist()
    
    