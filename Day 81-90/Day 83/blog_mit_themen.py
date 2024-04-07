import os
from flask import Flask,redirect,request

os.chdir(os.path.dirname(os.path.realpath(__file__)))

app=Flask(__name__,static_url_path='/static')

def get_theme(theme):
    themes={
        "default":"style-blog-post-default.css",
        "1":"style-blog-post-style-1.css",
        "2":"style-blog-post-style-2.css"
    }
    if theme is None:
        return themes['default']
    else:
        return themes[str(theme)]

@app.route('/')
def linktree():
    link1='/1'
    title_link1='1st Blog Post'
    link2 = '/2'
    title_link2='2nd Blog Post'
    with open("template/linktree-template.html","r",encoding="UTF-8") as f:
        page = f.read()
    page = page.replace("{link1}",link1)
    page = page.replace("{link2}",link2)
    page = page.replace("{title_link1}",title_link1)
    page = page.replace("{title_link2}",title_link2)
    
    return page

@app.route('/1')
def first_blog():
    stylesheet=get_theme(request.args.get("theme"))
    date = '5th April'
    title = 'My First Blog Post'
    text = 'Hey guys just trying out how i can Post stuff here \n\n\n Does this work'
    image = 'Day 77.JPG'
    back = "/"
    with open("template/blog-template.html","r",encoding="UTF-8") as f:
        page = f.read()
    page = page.replace("{date}",date)
    page = page.replace("{title}",title)
    page = page.replace("{text}",text)
    page = page.replace("{image}",image)
    page = page.replace("{back}",back)
    page= page.replace("{stylesheet}",stylesheet)
    return page

@app.route("/2")
def second_blog():
    stylesheet=get_theme(request.args.get("theme"))
    date = '6th April'
    title = 'My Second Blog Post'
    text = 'Finally got this shit to work\n Good Stuff'
    image = 'working.JPG'
    back = "/"
    with open("template/blog-template.html","r",encoding="UTF-8") as f:
        page = f.read()
    page = page.replace("{date}",date)
    page = page.replace("{title}",title)
    page = page.replace("{text}",text)
    page = page.replace("{image}",image)
    page = page.replace("{back}",back)
    page= page.replace("{stylesheet}",stylesheet)
    return page

@app.route("/3")
def redircet():
    return redirect("/")

app.run(host='0.0.0.0',port=81)