import os
import json
import requests


os.chdir(os.path.dirname(os.path.realpath(__file__)))

FOLDER_PATH="user_pictures"

def get_user():

    result = requests.get("https://randomuser.me/api/",timeout=5)
    if result.status_code != 200:
        print("API ERROR")
    
    user = result.json() #a dictionary containing the user's data
    name = f"""{user["results"][0]["name"]["first"]}_{user["results"][0]["name"]["last"]} """
    
    image = f"""{user["results"][0]["picture"]["medium"]}"""
    picture = requests.get(image,timeout=5)
    

    os.makedirs(FOLDER_PATH,exist_ok=True)
    
    with open(f"{FOLDER_PATH}/{name}.jpg","wb") as f:
        f.write(picture.content)


def main():
    for _ in range(10):
        get_user()
    print("done") 

if __name__ == "__main__":
    main()