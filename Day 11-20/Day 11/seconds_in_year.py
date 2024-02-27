leap_year = input("Is it a leap year? Y/N: ")


if leap_year.lower() == "y":
    leap_year = True
elif leap_year.lower() == "n":
    leap_year = False
else:
    print("Please answer the question with Y or N")
    
try:
    if leap_year is True:
        days = 366
    elif leap_year is False:
        days = 365
    seconds = days*24*60*60
    print("A year has", seconds,"seconds.")
except NameError:
    print("or else it wont work :)")
