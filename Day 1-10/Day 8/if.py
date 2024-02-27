name = input("What is your name?\n")
day = input("What day do we have today?\n")
activities = input("What did you do today?\n")

if day.lower() == "monday":
    print(f"Ah \33[34m{name}\33[0m, my condolences. I know that Mondays suck, but I hope that {activities} was at least fun :)")
elif day.lower() == "tuesday":
    if name.lower() == "john":
        print(f"Hey \33[34mJohn\33[0m, I hope you lost at {activities} and had a bad {day} :)")
    else:
        print(f"Hey \33[34m{name}\33[0m, you'll manage. At least you did {activities} today.")
elif day.lower() == "wednesday":
    print(f"Halfway there, champ.\nI am cheering you on \33[34m{name}\33[0m.")
elif day.lower() == "thursday":
    print(f"Almost there, \33[34m{name}\33[0m! Keep going and make the most out of your {day}.")
elif day.lower() == "friday":
    print(f"Happy {day}, \33[34m{name}\33[0m! It's almost the weekend, so finish strong and enjoy your activities.")
elif day.lower() == "saturday":
    print(f"Hello, \33[34m{name}\33[0m! I hope you're having a fantastic {day}. What exciting things are you up to?")
elif day.lower() == "sunday":
    print(f"Chill out, \33[34m{name}\33[0m! It's {day}, a perfect day to relax and recharge for the upcoming week.")
else:
    print("Invalid day input. Please enter a valid day of the week.")
