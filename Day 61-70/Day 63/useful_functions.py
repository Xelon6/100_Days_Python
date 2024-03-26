import os
import time
import json

FILE_NAME = "pizza.orders"

inventory = []


#setzt working directory zu jeztigen directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))


def clear_console():
    """cleared console auf win und unix"""
    os.system('clear' if os.name == 'posix' else 'cls')


def check_for_file(file):
    '''schaut ob file da is wenn nicht ladet leere list'''
    try:
        with open(FILE_NAME, "r", encoding="UTF-8") as file:
            inventory = json.load(file)
    except FileNotFoundError:
        print("No existing File starting with a blank one")
        time.sleep(1.5)
        clear_console()
        # Handle the case when the file does not exist


def save_to_file():
    '''save to file'''
    with open(FILE_NAME,"w",encoding="UTF-8") as f:
        json.dump(inventory,f)

if __name__ == "__main__":
    main()

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