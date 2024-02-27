birth_year = input("What year were you born in? ")

try:
    if 1925 <= int(birth_year) <= 1946:
        print("Your generation is called: Traditionalists")
    elif 1947 <= int(birth_year) <= 1964:
        print("Your generation is called: Baby Boomers")
    elif 1965 <= int(birth_year) <= 1981:
        print("Your generation is called: Generation X")
    elif 1982 <= int(birth_year) <= 1995:
        print("Your generation is called: Millenials")
    elif 1996 <= int(birth_year) <= 2015:
        print("Your generation is called: Generation Z")
    elif 2016 <= int(birth_year) <= 2023:
        print("Your generation is called: Generation Alpha")
    else:
        print("Your birthyear is not in the db yet.")
except ValueError:
    print("Please Enter a whole Number")
