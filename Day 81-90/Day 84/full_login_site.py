from flask import Flask,request,redirect
import os
import json


os.chdir(os.path.dirname(os.path.realpath(__file__)))

def save_to_file(file_name,data):
    '''save to file'''
    with open(file_name,"w",encoding="UTF-8") as f:
        json.dump(data,f)

def read_file(file_name):
    with open(file_name,"r", encoding="UTF-8") as f:
        return json.load(f)

def check_file(filename):
    try:
        with open(filename, 'r',encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) == 0:
                return False
            else:
                return True
    except FileNotFoundError:
        return False





FILE_NAME = "user_data.json"

app = Flask(__name__)

@app.route('/')
def login():
    with open("template/login.html","r",encoding="UTF-8") as f:
        page = f.read()
    
    return page


@app.route('/register')
def register():
    title = "Register"
    action = "check"
    button = "Register"
    typ = "register"
    with open("template/register.html","r",encoding="UTF-8") as f:
        page = f.read()
        page = page.replace("{title}",title)
        page = page.replace("{action}",action)
        page = page.replace("{button}",button)
        page = page.replace("{typ}",typ)
    return page


@app.route('/change',methods=["POST"])
def change():
    form = request.form
    user = form['username']
    title = "Change Password"
    action = "check"
    button = "Save Changes"
    typ = "change"
    with open("template/change_pw.html","r",encoding="UTF-8") as f:
        page = f.read()
        page = page.replace("{title}",title)
        page = page.replace("{action}",action)
        page = page.replace("{button}",button)
        page = page.replace("{typ}",typ)
        page = page.replace("{user}",user)
    return page

@app.route('/check',methods=["POST"])
def check():
    form = request.form
    
    
    if form["type"] == "register":
        try:
            users = read_file(FILE_NAME)
        except (FileNotFoundError, json.JSONDecodeError):
            users = {}
        if form["username"] in users:
            return "Username taken"
        else:
            username = form["username"]
            password = form["password"]
            users[username]={"password":password}
            save_to_file(FILE_NAME,users)
        return redirect("/")

    elif form["type"] == "change":
        username = form["username"]
        password = form["password"]
        new_password = form["new_password"]
        
        users = read_file(FILE_NAME)
            
        if password == users[username]["password"]:
            users[username]["password"] = new_password
            save_to_file(FILE_NAME,users)
            return redirect('/')
        
        else:
            return "Wrong Password"
    else:
        return "Error 1"
        
        


@app.route('/profile',methods=["POST"])
def profile():
    form = request.form
    is_there=check_file(FILE_NAME)
    if is_there is False:
        return "Please Register first<br><br><form action='/' method='GET'><input type='submit' value='Go Back to the Login Site'></form>"
    username = form["username"]
    password = form["password"]
    users = read_file(FILE_NAME)
    
    
    
    
    if form["username"] in users and password == users[username]["password"]:
        with open("template/profile.html","r",encoding="UTF-8") as f:
            page = f.read()
            page = page.replace("{user}",username)
        return page
    else:
        return "Wrong Username or Password"

    

app.run('0.0.0.0',port=81)