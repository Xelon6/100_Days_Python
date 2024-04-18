import os
import requests
import json
from flask import Flask,request,redirect,url_for

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#const

FILE_NAME="jokes.json"

#functions


def get_joke():
    result = requests.get("https://icanhazdadjoke.com/", headers={"accept":"application/json"},timeout=5) 
    if result.status_code != 200:
        print("API Error")
    
    joke = result.json()
    return joke["id"],joke["joke"]

def saved_jokes(unique_id):
    result = requests.get(f"https://icanhazdadjoke.com/j/{unique_id}", headers={"accept":"application/json"},timeout=5) 
    if result.status_code != 200:
        print("API Error")
    
    joke = result.json()
    return joke["joke"]


def save_to_file(data,file_path):
    with open(file_path,"w",encoding="UTF-8") as f:
        json.dump(data,f)

def read_template(template):
    with open(f"template/{template}.html","r",encoding="UTF-8") as f:
        return f.read()

def read_json(file):
    with open(f"{file}","r",encoding="UTF-8") as f:
        return json.load(f)

#flask

app=Flask(__name__,static_folder="static")

@app.route('/')
def index():
    #vars
    page = read_template("index")
    unique_id,joke = get_joke()
    
    #replace
    page=page.replace("{joke}",joke)
    page= page.replace("{id}",unique_id)
    
    return page

@app.route("/save",methods=["POST"])
def save_joke():
    form=request.form
    unique_id=form["joke_id"]

    
    try:
        jokes=read_json(FILE_NAME)
        if len(jokes) == 0:
            jokes=[]
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        jokes = []
    if unique_id not in jokes:
        jokes.append(unique_id)
    save_to_file(jokes,FILE_NAME)
    return redirect(url_for("index"))

@app.route("/view")
def view():
    page=read_template("view")
    joke_list=""
    try:
        jokes=read_json(FILE_NAME)
        if len(jokes) <= 2:
            return "No Jokes saved yet"
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        return "No Jokes saved yet"
    
    for joke_id in jokes:
        joke = saved_jokes(joke_id)
        joke_list += f"<li class='joke'>{joke}</li><br>"

    page = page.replace("{joke}",joke_list)
    
    return page


app.run("0.0.0.0",port=81)