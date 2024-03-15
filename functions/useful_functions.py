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
