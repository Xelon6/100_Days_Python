def factorial(value):
    if value == 1:
        return 1
    else:
        return value * factorial(value-1)

number= int(input("Enter the number you want the factorial Value of\n> "))


print(f"The factorial of {number} is {factorial(number)}")