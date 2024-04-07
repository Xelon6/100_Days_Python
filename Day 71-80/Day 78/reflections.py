from flask import Flask
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))


app = Flask(__name__)


def get_range(day):
    day_number = int(day)
    if 1 <= day_number <= 10:
        return "1-10"
    elif 11 <= day_number <= 20:
        return "11-20"
    elif 21 <= day_number <= 30:
        return "21-30"
    elif 31 <= day_number <= 40:
        return "31-40"
    elif 41 <= day_number <= 50:
        return "41-50"
    elif 51 <= day_number <= 60:
        return "51-60"
    elif 61 <= day_number <= 70:
        return "61-70"
    elif 71 <= day_number <= 80:
        return "71-80"

@app.route('/<pageNumber>')
def index(pageNumber):
    number = str(pageNumber)

        
    try:
        day = int(pageNumber)
    except ValueError:
        return "Not a valid Number"
    day_range = get_range(day)
    link = f"https://github.com/Xelon6/100_Days_Python/tree/main/Day%20{day_range}/Day%20{str(day)}"
    
    with open("template/wordlist.txt","r",encoding="UTF-8") as f:
        texts = f.readlines()
        if day <= len(texts):
            text = texts[day-1]
            link_text = "See my Code here"
        else:
            link_text = ""
            text= "Day not done yet"

    with open("template/reflection.html","r",encoding="UTF-8") as f:
        page = f.read()
        page = page.replace('{number}',number)
        page = page.replace('{link}',link)
        page = page.replace('{text}',text)
        page = page.replace('{link_text}',link_text)
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)