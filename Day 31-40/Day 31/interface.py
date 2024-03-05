
def color_change(color, text):
    color_code = None

    if color.lower() == "red":
        color_code = "\33[31m"
    elif color.lower() == "blue":
        color_code = "\33[34m"
    elif color.lower() == "green":
        color_code = "\33[32m"
    elif color.lower() == "yellow":
        color_code = "\33[33m"
    elif color.lower() == "purple":
        color_code = "\33[35m"
    elif color.lower() == "cyan":
        color_code = "\33[36m"
    elif color.lower() == "white":
        color_code = "\33[37m"
    else:
        # Default to no color change if the input color is not recognized
        return text

    colored_text = f"{color_code}{text}\33[0m"
    return colored_text

print("")
print(f"{color_change("blue","Login Screen"):^35}\n")
print(f"{color_change("green","Username: "):<50}")
print(f"{color_change("red","Password: "):<50}")
print(f"\n{color_change("purple","Remember to keep your Password hidden"):^35}")
