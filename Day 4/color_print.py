print(
    "Welcome to your adventure simulator.\nI am going to ask you a bunch of questions and then create an epic story with you as the star!"
)

name = input("What is your name? ")
enemy_name = input("What is your worst enemy’s name? ")
superpower = input("What is your superpower? ")
location = input("Where do you live? ")
favorite_food = input("What is your favorite food? ")

print(
    f"Hello \33[34m{name}\33[0m!\nYour ability to \33[36m{superpower}\33[0m will make sure you never have to look at \33[31m{enemy_name}\33[0m again.\nGo eat \33[33m{favorite_food}\33[0m as you walk down the streets of \33[33m{location}\33[0m and use \33[36m{superpower}\33[0m for good and not evil!"
)
