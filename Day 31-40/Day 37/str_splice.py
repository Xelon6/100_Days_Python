#erste 3 buchstaben vom vornamen
#ersten 3 buchstaben vom nachnamen
# erster name

def name(art):
    return input(f"Enter your {str(art)} name: ").strip().lower()


first_name = name("first")
last_name = name("last")
father_name = name("fathers")
mother_name = name("mothers")

def first_3(word):
    first_3_l = word[0:3]
    return first_3_l

def join_letters(first,second):
    added = f"{first}{second}"
    return added.capitalize()

print("Your Name is:")
print()
print(f"{join_letters(first_3(first_name),first_3(last_name))} {join_letters(first_3(father_name),first_3(mother_name))}")
#zweiter name ersten buchstaben vom namen der mutter + ersten 3 vom vater
