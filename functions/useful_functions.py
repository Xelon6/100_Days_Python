import os
import time
import json

FILE_NAME = "pizza.orders"

inventory = []


#setzt working directory zu jeztigen directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#erstellt einen Ordner wenn noch keiner mit dem selben namen existiert
os.makedirs(FOLDER_PATH,exist_ok=True)

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


def check_file(filename):
    """schaut ob es die datei gibt und ob was drinnen steht"""
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) == 0:
                return False
            else:
                return True
    except FileNotFoundError:
        return False

def save_to_file():
    '''save to file'''
    with open(FILE_NAME,"w",encoding="UTF-8") as f:
        json.dump(inventory,f)

def read_json(file_name):
    """liest eine datei"""
    with open(file_name, "r", encoding="UTF-8") as f:
        return json.load(f)


def hash_password(password):
    '''hashes pw in sha256'''
    import hashlib
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


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


#js button for html
#<button type="submit" onclick="location.href='url_for'">Go back</button>