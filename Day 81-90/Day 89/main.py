import os
import json
import hashlib
import secrets
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask,request,redirect,url_for,session




#const 

os.chdir(os.path.dirname(os.path.realpath(__file__)))
load_dotenv()

admin_id=os.getenv("ADMIN_ID")
admin_username=os.getenv("ADMIN_USER")
admin_pass = os.getenv("ADMIN_PASS")
admin_salt=os.getenv("ADMIN_SALT")




FILE_NAME_MESSAGES="messages.json"
USER_DATA="user_data.json"
app = Flask(__name__, static_url_path='/static')
app.secret_key = os.getenv("SESSION_KEY")

#Functions


def save_to_file(file_name, data):
    '''save to file'''
    with open(file_name, "w", encoding="UTF-8") as f:
        json.dump(data, f)


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


def read_json(file_name):
    """liest eine datei"""
    with open(file_name, "r", encoding="UTF-8") as f:
        return json.load(f)

def read_template(file_name):
    """liest eine datei"""
    with open(f"template/{file_name}", "r", encoding="UTF-8") as f:
        return f.read()



def hash_password(password):
    '''hashes pw in sha256'''
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


def generate_pw(password):
    """adds salt to hashing"""
    salt = secrets.token_hex(8)
    hashed_pw = hash_password(f"{salt}{password}")
    return salt,hashed_pw

def check_password(entered,salt,password):
    """überprüft ob das eingebene password gleich das gespeicherete ist"""

    if hash_password(f"{salt}{entered}") == password:
        return True
    else:
        return False


def find_smallest_available_user_id(user_data):
    """findet die kleineste verfügbare user id"""
    existing_user_ids = user_data.keys()
    max_user_id = max(map(int, existing_user_ids)) if existing_user_ids else 0
    return min(set(range(1, max_user_id + 2)) - set(map(int, existing_user_ids)))


def username_exists(user_data, username):
    """Überprüft, ob der Benutzername bereits vorhanden ist."""
    for user_info in user_data.values():
        if user_info["username"] == username:
            return True
    return False


def generate_login():
    """generiert einen login Knopf"""
    style = """<link rel="stylesheet" href="static/style.css">"""
    button_to_login="""<button class="button" type="button" onclick="location.href='/'">Go to Login</button>"""
    return f"{style}Please login first<br>{button_to_login}"

ADMIN_PASS_HASH=hash_password(f"{admin_salt}{admin_pass}")

#webpages visible

@app.route('/')
def welcome():
    """welcome/login Seite"""

    if not session.get("loggedin", True):
        return redirect(url_for("chat"))
    #vars
    style="style.css"
    button2 = """<button type="button" class="button" onclick="location.href='/register'">Register</button>"""
    use="Login"
    action="auth"
    button1_text="Login"

    #template laden
    page = read_template("login.html")

    #template anpassen
    page=page.replace("{style}",style)
    page = page.replace("{button2}",button2)
    page = page.replace("{use}",use)
    page = page.replace("{action}",action)
    page = page.replace("{button1_text}",button1_text)

    return page

@app.route('/register')
def register():
    """Register Seite"""
    #vars
    style="style.css"
    button2 =  """<br>"""
    use="Register"
    action="reg"
    button1_text="Register"

    #template laden
    page = read_template("login.html")

    #template anpassen
    page=page.replace("{style}",style)
    page = page.replace("{button2}",button2)
    page = page.replace("{use}",use)
    page = page.replace("{action}",action)
    page = page.replace("{button1_text}",button1_text)

    return page

@app.route("/chat")
def chat():
    """Chatroom"""
    #check ob er eh eingeloggt ist
    if not session.get("loggedin", False):
        return generate_login()
    
    style="style.css"
    page=read_template("chatroom.html")
    page=page.replace("{user}",session["username"])

    #messages anzeigen
    try:
        messages=""
        posts=read_json(FILE_NAME_MESSAGES)

        # Sortieren der Nachrichten nach Schlüssel (Datum)
        sorted_keys = sorted(posts.keys(), reverse=True)



        
        
        # Die ersten 5 Nachrichten auswählen
        latest_messages = []
        for key in sorted_keys[:5]:
            message = posts[key]
            username = message["username"]
            time = message["time"]
            text=message["message"]
            if session.get("admin", True):
                delete_message = f"""
                                <form action="/delete" method="post">
                                <button type="submit" class="button">
                                <input type="hidden" name="key" value="{key}">Delete</button>
                                </form>"""
            else:
                delete_message = ""
            latest_messages.append(f"""<div class="chat-text">{time} - <span class="username">{username}</span>: {text} {delete_message}</div><hr>""")

        # Nachrichten in HTML-Format umwandeln
        messages = "".join(latest_messages)

    # wenn keine Nachrichten da sind
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        messages = "No Messages yet :("

    #page replaces
    page=page.replace("{placeholder}",messages)
    page=page.replace("{style}",style)
    return page

@app.route("/settings")
def settings():
    """Profile settings"""
    if not session.get("loggedin", False):
        return generate_login()
    style="style.css"
    page=read_template("settings.html")
    page=page.replace("{style}",style)

    return page

@app.route('/delete_acc')
def delete_acc():
    """delete account confirmation"""
    if not session.get("loggedin", False):
        return generate_login()
    #vars
    page=read_template("delete.html")
    use="Delete Account"
    style="style.css"
    button1_text="Delete Account"
    button2 = f"""<button class="button" type="submit" onclick="location.href='{url_for("settings")}'" class="button">Go back</button>"""
    new="""<input type="hidden" name="delete" id="delete" value="True">"""
    new_confirm=""
    action=url_for("delete_acc_red")

    #replace

    page=page.replace("{style}",style)
    page=page.replace("{use}",use)
    page=page.replace("{new}",new)
    page=page.replace("{new_confirm}",new_confirm)
    page=page.replace("{button1_text}",button1_text)
    page=page.replace("{button2}",button2)
    page=page.replace("{action}",action)



    return page

@app.route('/change_pw')
def change_pw():
    """change password confirmation"""
    if not session.get("loggedin", False):
        return generate_login()
    #vars
    page=read_template("change.html")
    use="Change Password"
    style="style.css"
    button1_text="Change Password"
    button2 = f"""<button class="button" type="submit" onclick="location.href='{url_for("settings")}'" class="button">Go back</button>"""
    action=url_for("change_confirm")
    typ="change_pw"
    new_type="Password"
    input_type = "password"
    #replace
    
    page=page.replace("{style}",style)
    page=page.replace("{use}",use)

    page=page.replace("{button1_text}",button1_text)
    page=page.replace("{button2}",button2)
    page=page.replace("{action}",action)
    page=page.replace("{typ}",typ)
    page=page.replace("{new_type}",new_type)
    page=page.replace("{input_type}",input_type)
    
    
    return page



@app.route('/change_user')
def change_user():
    """change password confirmation"""
    if not session.get("loggedin", False):
        return generate_login()
    #vars
    page=read_template("change.html")
    use="Change Username"
    style="style.css"
    button1_text="Change Username"
    button2 = f"""<button class="button" type="submit" onclick="location.href='{url_for("settings")}'" class="button">Go back</button>"""
    action=url_for("change_confirm")
    typ="change_username"
    new_type="Username"
    input_type = "text"
    #replace
    
    page=page.replace("{style}",style)
    page=page.replace("{use}",use)

    page=page.replace("{button1_text}",button1_text)
    page=page.replace("{button2}",button2)
    page=page.replace("{action}",action)
    page=page.replace("{typ}",typ)
    page=page.replace("{new_type}",new_type)
    page=page.replace("{input_type}",input_type)
    
    
    return page




# hidden pages

@app.route('/auth',methods=["POST"])
def auth():
    """checkt ob die login daten passen"""
    form= request.form
    username = form["username"]
    entered_password = form["password"]
    back_button="""<br><button class="button" type="button" onclick="location.href='/'">Go Back</button>"""



    try:
        users=read_json(USER_DATA)
        if not users:
            users={"0":{"username":admin_username,"password":ADMIN_PASS_HASH,"salt":admin_salt}}
            save_to_file(USER_DATA,users)
            return f"No Users Registered yet{back_button}"
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        users={"0":{"username":admin_username,"password":ADMIN_PASS_HASH,"salt":admin_salt}}
        save_to_file(USER_DATA,users)
        return f"No Users Registered yet{back_button}"

    for user_id, user_data in users.items():

        if username == user_data["username"]:
            if check_password(entered_password,user_data["salt"],user_data["password"]):
                session["loggedin"] = True
                session["user_id"] = user_id
                session["username"]=username
                if session["user_id"] == "0":
                    session["admin"] = True
                    
                else:
                    session["admin"] = False
                return redirect(url_for("chat"))

    return f"""<script>
    alert("Wrong Password/Username Combo");
    window.location.href = "{url_for('welcome')}";
</script>"""



@app.route('/reg',methods=["POST"])
def reg():
    """erstellt Users und weist user id zu"""
    form = request.form
    username = form["username"]
    salt,password = generate_pw(form["password"])


    try:
        users=read_json(USER_DATA)
        if not users:
            users = {"0":{"username":admin_username,"password":ADMIN_PASS_HASH,"salt":admin_salt}}

    except (FileNotFoundError,json.decoder.JSONDecodeError):
        users={"0":{"username":admin_username,"password":ADMIN_PASS_HASH,"salt":admin_salt}}
        save_to_file(USER_DATA,users)


    if username_exists(users,username):
        return """Username taken<br><button type="button" class="button" onclick="location.href='/register'">Go back</button>"""



    user_id = find_smallest_available_user_id(users)
    users[user_id]={"username":username,"password":password,"salt":salt}


    save_to_file(USER_DATA,users)




    return redirect(url_for("welcome"))


@app.route('/post',methods=["POST"])
def post():
    """messages posten"""
    if not session.get("loggedin", False):
        return generate_login()
    form = request.form
    message=form["message"]
    time = datetime.now()
    user_id= session["user_id"]
    time_seconds= time.strftime("%Y-%m-%d %H:%M:%S")
    time_key=time.strftime("%Y-%m-%d/%H:%M:%S.%f")
    users=read_json(USER_DATA)
    username = users[user_id]["username"]

    try:
        posts=read_json(FILE_NAME_MESSAGES)
        if not posts:
            posts={}
        posts[time_key]={"user_id":user_id,"message":message,"time":time_seconds,"username":username}
        save_to_file(FILE_NAME_MESSAGES,posts)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        posts={}
        posts[time_key]={"user_id":user_id,"message":message,"time":time_seconds,"username":username}
        save_to_file(FILE_NAME_MESSAGES,posts)
    return redirect(url_for("chat"))

@app.route('/delete',methods=["POST"])
def delete():
    """löscht chat nachrichten"""
    form = request.form

    key = form["key"]

    try:
        messages=read_json(FILE_NAME_MESSAGES)
        messages.pop(key)
        save_to_file(FILE_NAME_MESSAGES,messages)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        pass

    return redirect(url_for("chat"))

@app.route('/delete-acc-red',methods=["POST"])
def delete_acc_red():
    """löscht user"""
    if not session.get("loggedin", False):
        return generate_login()
    form=request.form
    user_id=session["user_id"]


    if form["delete"] == "True":

        try:
            users = read_json(USER_DATA)

            salt = users[user_id]["salt"] 
            password= users[user_id]["password"]
            
            check=check_password(form["password"],salt,password)

            if check:
                users.pop(user_id)
                save_to_file(USER_DATA,users)
                return redirect(url_for("reset"))
            else: 
                return f"""<script>
    alert("Wrong Password/Username Combo");
    window.location.href = "{url_for('settings')}";
</script>"""
            
        except(FileNotFoundError,json.decoder.JSONDecodeError):
            return redirect(url_for("settings"))


@app.route('/change_confirm',methods=["POST"])
def change_confirm():
    """schaut ob pw passt und führt dann die änderungen durch"""
    if not session.get("loggedin", False):
        return generate_login()
    form = request.form
    type_of_change=form["typ"]
    wrong_pw=f"""<script>
    alert("Wrong Password");
    window.location.href = "{url_for('settings')}";
</script>"""
    user_id=session["user_id"]

    try:
        users=read_json(USER_DATA)

        salt = users[user_id]["salt"] 
        password= users[user_id]["password"]
        check=check_password(form["password"],salt,password)
        change=form["new"]
        
        if check:
            if type_of_change=="change_pw":
                users[user_id]["salt"],users[user_id]["password"]=generate_pw(change)


            elif type_of_change=="change_username":
                users[user_id]["username"]=change

            save_to_file(USER_DATA,users)
        else:
            return wrong_pw
    except(FileNotFoundError,json.decoder.JSONDecodeError):
        return f"""<script>
    alert("Error");
    window.location.href = "{url_for('settings')}";
</script>"""



    return redirect(url_for("reset"))


@app.route('/reset')
def reset():
    """logout Funktion"""
    session.clear()
    return redirect(url_for("welcome"))

app.run("0.0.0.0",port=81)
