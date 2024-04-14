import os
import json
from flask import Flask, session, redirect, request, make_response, url_for


#const here

os.chdir(os.path.dirname(os.path.realpath(__file__)))

admin_user = os.environ["ADMIN_USERNAME"]
user_id = os.environ["USER_ID"]

app = Flask(__name__, static_url_path='/static')
app.secret_key = os.environ["SESSION_KEY"]

FILE_NAME = "posts.json"

# functions here


def save_to_file(file_name, data):
    '''save to file'''
    with open(file_name, "w", encoding="UTF-8") as f:
        json.dump(data, f)


def check_file(filename):
    try:
        with open(filename, 'r', encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) == 0:
                return False
            else:
                return True
    except FileNotFoundError:
        return False


def read_file(file_name):
    with open(file_name, "r", encoding="UTF-8") as f:
        return f.read()


def generate_select_options(posts):
    options = ""
    for item in posts:
        options += f'<option value="{item[1]}">{item[1]}</option>'
    return options


#website here


@app.route('/')
def index():
    no_post = """<div class="post">
    <h3>No Posts yet</h3>
    </div>"""
    logout = """<button type="button" onclick="location.href='/reset'">Logout</button>"""
    admin_dash = """<form action="/auth"><button type="submit">Admin Dashboard</button></form>"""
    style = "/static/style.css"
    page = read_file("template/index.html")
    page = page.replace("{style}", style)

    #replit login system

    login_id = request.headers["X-Replit-User-Id"]
    if login_id:
        if login_id == user_id:
            page = page.replace("{button}",
                                f"""{admin_dash}<br>{logout}<br>""")
        else:
            page = page.replace("{button}", f"""{logout}<br>""")

    else:
        # Wenn nicht eingeloggt, zeige den Login-Button an
        page = page.replace(
            "{button}",
            """<button onclick="LoginWithReplit()"> Login </button><br>""")

    try:
        with open(FILE_NAME, 'r', encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) <= 2:
                page += no_post
                page += "<br>"
            else:
                page += "<br>"
                page += "<br>"
                posts = json.loads(content)
                for item in reversed(posts):
                    date = item[0]
                    title = item[1]
                    text = item[2]
                    entry = f"""<div class="post">
                            <h2>{date}</h2>
                            <h3>{title}</h3>
                            <p>{text}</p>
                            </div>"""
                    page += entry
                    page += "<br>"

    except FileNotFoundError:
        page += """<div class="post">
                            <h3>No Posts yet</h3>
                            </div>"""
    return page


@app.route('/auth')
def auth():
    login_id = request.headers["X-Replit-User-Id"]
    if session.get("loggedin"):
        return redirect('/')
    if login_id == user_id:
        logged_in = True
        session["loggedin"] = logged_in
        session["admin"] = True
        return redirect('/profile')
    else:
        return "You are not an admin<br><br><form action='/' method='GET'><input type='submit' value='Go Back to the main Page'></form>"


@app.route('/profile')
def profile():
    user = request.headers["X-Replit-User-Name"]
    button = """<button type="button" onclick="location.href='/reset'">Logout</button>"""
    style = "/static/style.css"
    no_post = """<div class="post">
                            <h3>No Posts yet</h3>
                            </div>"""

    if request.headers["X-Replit-User-Id"] != user_id:
        return "You are not an admin<br><br><form action='/' method='GET'><input type='submit' value='Go Back to the main Page'></form>"
    page = read_file("template/profile.html")

    try:
        with open(FILE_NAME, 'r', encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) <= 2:
                page += no_post
                page = page.replace("{delete}", "<br>")
            else:
                posts = json.loads(content)
                delete = f"""
                <form method='post' action='/delete_post'>
                    <select name='post_title'>
                    {generate_select_options(posts)}
                    </select>
                    <input type='submit' value='Delete Post'>
                </form>
                """
                page = page.replace("{delete}", delete)
                page += "<br>"
                page += "<br>"

                for item in reversed(posts):
                    date = item[0]
                    title = item[1]
                    text = item[2]
                    entry = f"""<div class="post">
                            <h2>{date}</h2>
                            <h3>{title}</h3>
                            <p>{text}</p>
                            </div>"""
                    page += entry
                    page += "<br>"

    except FileNotFoundError:
        page += no_post
        page = page.replace("{delete}", "<br>")

    page = page.replace("{button}", button)
    page = page.replace("{style}", style)
    page = page.replace("{user}", user)
    return page


@app.route('/reset')
def reset():

    session.clear()

    # Get hostname for setting the correct domain in the cookie
    hostname = request.host

    response = make_response(redirect(url_for('index')))

    # Clearing REPL_AUTH cookie for the specified domain
    response.delete_cookie('REPL_AUTH', domain='.' + hostname)

    return response


@app.route('/save', methods=["POST"])
def save():
    if not session.get("loggedin"):
        return redirect('/')
    form = request.form
    try:
        with open(FILE_NAME, 'r', encoding="UTF-8") as file:
            content = file.read()
            if len(content.strip()) == 0:
                posts = []
            else:
                posts = json.loads(content)
    except FileNotFoundError:
        posts = []
    posts.append([form["date"], form["title"], form["text"]])
    save_to_file(FILE_NAME, posts)
    return redirect('/profile')


@app.route('/delete_post', methods=["POST"])
def delete_post():
    if not session.get("loggedin"):
        return redirect('/')
    form = request.form.get('post_title')
    content = read_file(FILE_NAME)
    posts = json.loads(content)
    updated_posts = [post for post in posts if post[1] != form]
    save_to_file(FILE_NAME, updated_posts)
    return redirect('/')


app.run("0.0.0.0", port=81)
