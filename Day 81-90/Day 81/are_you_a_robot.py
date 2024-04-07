from flask import Flask,request
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

@app.route('/')
def index():
    with open("template/form.html","r",encoding="UTF-8") as f:
        page=f.read()
    return page

@app.route('/process',methods=["POST"])
def process():
    answers = request.form
    if answers["choice-radio"] == "no" and answers["food"] == "Human food" and answers["sum"] == "10":
        return "You are a Human :)"
    else:
        return "I knew it you were Robot!"
    return answers

app.run('0.0.0.0',port=81)