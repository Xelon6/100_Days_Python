from flask import Flask,request
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

@app.route('/')
def index():
    with open("template/form.html","r",encoding="UTF-8") as f:
        page = f.read()
    
    return page

@app.route('/login',methods=["POST"])
def login():
    users={}
    users['david']={'password':'132','Email':'b@b'}
    users['jeff']={'password':'132','Email':'a@b'}
    users['chris']={'password':'132','Email':'c@b'}

    form = request.form
    username = form["username"]
    password = form["password"]
    email = form["Email"]
    
    
    if username in users and password == users[username]['password'] and email == users[username]['Email']:
        return "You are logged in"
    else:
        return "False Password, Username or Email"
        

app.run('0.0.0.0',port=81)