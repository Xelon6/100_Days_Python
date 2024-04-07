from flask import Flask, request

app = Flask(__name__)




@app.route('/', methods=["GET"])
def index():
    lang = request.args.get('lang')
    
    if lang is None:
        return """<form action="/" method="GET">
        <button type="submit" name="lang" value="eng">English</button>
    </form>
    <form action="/" method="GET">
        <button type="submit" name="lang" value="ger">German</button>
    </form>"""
    
    if lang.lower() == 'eng':
        return """<p>Hey There the site is now in english</p> <form action="/" method="GET"><button type="submit" href="/">Go back</button></form>
    """
    
    elif lang.lower() == "ger":
        return """<p>Servas die seite is jetzt auf deutsch</p> <form action="/" method="GET"><button type="submit" href="/">Go back</button></form>
    """

if __name__ == '__main__':
    app.run('0.0.0.0', port=81)
