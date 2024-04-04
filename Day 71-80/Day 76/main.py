from flask import Flask # Imports the flask library

app = Flask(__name__, static_url_path="/static") # Starts the Flask application.


@app.route('/') # Tells the code what to do if we've gone to our web address with just a / after the URL
def index(): # Tells the code which webpage to show. This subroutine will display the 'Hello from Flask' page
    page = """
        <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Index</title>
  <link href="../static/css/style-linktree.css" rel="stylesheet" type="text/css" />
</head>
    

   <body> 
   <div class=grey-banner>
   <h1>Meine Websiten</h1>
   </div>
   <br>
    <ul>
        <li>
            <a href="/linktree" class="linkbox">
                <h3>Linktree</h3>
            </a>
        </li>
        <br>
        <li>
            <a href="/portfolio" class="linkbox">
            <h3>Portfolio</h3>
        </a>

    </ul>
 
</body>

</html>
    """
    return page

@app.route('/linktree')
def linktree():
    page= """ 
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Link Tree</title>
  <link href="../static/css/style-linktree.css" rel="stylesheet" type="text/css" />
</head>

<body> 
    <img src="static/images-linktree/me.jpg">
    <<ul>
        <li>
            <a href="https://github.com/Xelon6" class="linkbox">
                <img src="static/images-linktree/githublogo.jpg" alt="GitHub Logo" class="logo">
                <h3>Github</h3>
            </a>
        </li>
        <br>
        <li>
            <a href="https://www.instagram.com" class="linkbox" target="_blank">
                <img src="static/images-linktree/insta-logo.png" alt="Insta Logo" class="logo">
            <h3>Instagram</h3>
        </a>
        </li>
        <br>
        <li>
            <a href="https://tryhackme.com/p/getting.into.it" class="linkbox" target="_blank">
                <img src="static/images-linktree/tryhackme-logo.png" alt="TryHackMe Logo" class="logo">
            <h3>TryHackMe</h3>
        </a>
        </li>
        <br>
        <li>
            <a href="https://replit.com/@Xelon6" class="linkbox" target="_blank">
                <img src="static/images-linktree/Replit_Logo.svg.png" alt="Replit Logo" class="logo">
            <h3>Replit</h3>
        </a>
        </li>
        <br>
        <li>
            <a href="/" class="linkbox">
            <h3>Go Back</h3>
        </a>
        </li>


    </ul>
 
</body>

</html>

    """
    return page

@app.route('/portfolio')
def portfolio():
    page = """
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Portfolio</title>
  <link href=static/css/style-portfolio.css rel="stylesheet" type="text/css" />
</head>

<body> 
  <div class="white-box">
    <h1>Davids Replit Projects</h1>
    <p>Es ist schwer die besten Projekte die ich bis jetzt gemacht habe zu finden, also zähle ich einfach die ersten 4 die mir eingefallen sind auf</p>
      
    <br>
    <br>
    <h4>Day 18</h4>
    <a href="/portfolio/Day_18">number guesser</a>
    <br>
    <br>
    <h4>Day 28</h4>
    <a href="/portfolio/Day_28">Charakter Battler</a>
    <br>
    <br>
    <h4>Day 39</h4>
    <a href="/portfolio/Day_39">Hangman</a>
    <br>
    <br>
    <h4>Day 47</h4>
    <a href="/portfolio/Day_47">Top Trumps</a>
    <br>
    <br>
    <br>

    <h3>Du findest Sämtliche Projekte auch auf meiner Github Seite</h3>
    <a href="https://github.com/Xelon6/100_Days_Python" target="_blank" class="git">Meine Github Seite</a>
    <br>
    <br>
    <a href="/" class="git">Go back</a>
  </div>
</body>

</html>

    """
    return page

@app.route('/portfolio/Day_18')
def number_guess():
    page = """
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Number guesser</title>
  <link href="../static/css/style-portfolio.css" rel="stylesheet" type="text/css" />
  <div class="grey-banner">
    <h1>Number guesser</h1>
    </div>
</head>

<body>
    <div class="white-box">
    <br>
    
    <br>
    <br>
    <h1 style="font-size: larger;">Details</h1>
    <br>
    <p style="font-size: medium;">Diese Projekt hat mich besonders interessiert.</p>
    <br>
    <p style="font-size: medium;">Das Projekt selber der wo man die random Nummer erraten muss ist ansich nichts besonderes. Ich habe es mir aber zur Aufgabe gemacht das Spiel zu automatisieren und dies war sehr interessant</p>
    <br>
    <ol>
        <li><br><img src="../static/images-portfolio/number_guess_1.jpg">
            <br>
            <p style="font-size: medium;">Man wird aufgefordert ein Nummer zwischen 1 und 1.000.000 zu erraten</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/number_guess_2.jpg">
            <br>
            <img src="../static/images-portfolio/number_guess_3.jpg">
            <br>
            <p style="font-size: medium;">Nach jedem Falschen Rate versuch wird einen angezeigt ob man zu niedrig oder zu hoch geraten hat.</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/number_guess_4.jpg">
            <p style="font-size: medium;">Wenn man die richtige Nummer errat wird einen angezeigt wie viele Versuche man braucht und man wird gefragt ob man noch eine Runde Spielen mag.</p>
        </li>
        <li>
            <br>
            <img src="../static/images-portfolio/number_guess_4.jpg">
            <p style="font-size: medium;">Ich wollte das ganze automatisieren.</p>
            <p style="font-size: medium;"> Also habe ich ein Script geschrieben welche das Nummer Rate Spiel als subprozess öffnet und danach die richtige Nummer automatisch erratet.</p>
        </li>
    </ol>

    <br><a href="https://github.com/Xelon6/100_Days_Python/tree/main/Day%2011-20/Day%2018" target="_blank" style="font-size: medium;">Github Link</a>
    <br><a href="/portfolio"style="font-size:medium;">Go back</a>
</div>
</body>
</html>
    """
    return page

@app.route('/portfolio/Day_28')
def character_battler():
    page  = """
    
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Charakter Battler Details</title>
  <link href="../static/css/style-portfolio.css" rel="stylesheet" type="text/css" />
  <div class="grey-banner">
    <h1>Charakter Battler</h1>
    </div>
</head>


<body>
    <div class="white-box">
    <br>
    
    <br>
    <br>
    <h1 style="font-size: larger;">Details</h1>
    <br>
    <p style="font-size: medium;">Diese Projekt lässt dich 2 Charakter erstellen und diese gegeinander Kämpfen lassen</p>
    <br>
    <ol>
        <li><br><img src="../static/images-portfolio/char_battler_1.jpg">
            <br>
            <p style="font-size: medium;">Als erstes kann man den Namen und die Rasse dieser Charakter auswählen oder diese Random generieren lassen</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/char_battler_2.jpg">
            <br>
            <p style="font-size: medium;">Danach wird gezeigt welche 2 Charakter gegeneinander kämpfen </p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/char_battler_3.jpg">
            <p style="font-size: medium;">Danach wird mittels eines Speed checks entschieden welcher der 2 Charakter angreift und dem anderen Schaden zufügt</p>
        </li>
        <li>
            <br>
            <img src="../static/images-portfolio/char_battler_4.jpg">
            <p style="font-size: medium;">Sollte ein Charakter keine Leben mehr haben wird der Gewinner festgelegt</p>
        </li>
    </ol>





 


    <br><a href="https://github.com/Xelon6/100_Days_Python/tree/main/Day%2021-30/Day%2028"  target="_blank" style="font-size: medium;">Github Link</a>

    <br><a href="/portfolio"style="font-size:medium;">Go back</a>
</div>
</body>
</html>
    """
    return page

@app.route('/portfolio/Day_39')
def hangman():
    page="""
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Hangman</title>
  <link href="../static/css/style-portfolio.css" rel="stylesheet" type="text/css" />
  <div class="grey-banner">
    <h1>Hangman</h1>
    </div>
</head>

<body>
    <div class="white-box">
    
    <br>
    
    <br>
    <br>
    <h1 style="font-size: larger;">Details</h1>
    <br>
    <p style="font-size: medium;">Diese Projekt ist ein einfaches Hangman Spiel. Es nimmt ein random Wort aus einer Wortliste und lässt es dich erraten</p>
    <br>
    <ol>
        <li><br><img src="../static/images-portfolio/hangman_1.jpg">
            <br>
            <p style="font-size: medium;">Man bekommt die leeren Buchstaben als _ angezeigt und sieht seine Leben</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/hangman_2.jpg">
            <br>
            <p style="font-size: medium;">Sollte man einen Buchstaben Falsch raten wird dieser angezeigt und 1 Leben abgezogen </p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/hangman_3.jpg">
            <p style="font-size: medium;">Richtige Buchstaben ersetzen die leeren _</p>
        </li>
        <li>
            <br>
            <img src="../static/images-portfolio/hangman_4.jpg">
            <p style="font-size: medium;">Yay das Wort wurde Richtig erraten</p>
        </li>
    </ol>

    
    <br><a href="https://github.com/Xelon6/100_Days_Python/tree/main/Day%2031-40/Day%2039"  target="_blank" style="font-size: medium;">Github Link</a>

    <br><a href="/portfolio"style="font-size:medium;">Go back</a>
</div>
    </body>
</html>
    """
    return page
    



@app.route('/portfolio/Day_47')
def top_trumps():
    page="""
    <!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Top Trumps</title>
  <link href="../static/css/style-portfolio.css" rel="stylesheet" type="text/css" />
  <div class="grey-banner">
    <h1>Top Trumps</h1>
    </div>
</head>

<body>
    <div class="white-box">
    <br>
    
    <br>
    <br>
    <h1 style="font-size: larger;">Details</h1>
    <br>
    <p style="font-size: medium;">Diese Projekt ist ein Spiel in welchem man gegen einen Computer spielt man kann mit selbst erstellten Charakteren oder mit den vorgefertigten spielen.</p>
    <br>
    <ol>
        <li><br><img src="../static/images-portfolio/Top_Trumps_1.jpg">
            <br>
            <p style="font-size: medium;">Als erstes Sieht man ein Menu mit mehreren Optionen</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/Top_Trumps_2.jpg">
            <br>
            <p style="font-size: medium;">Wählt man Battle aus Kann man sich seinen "Trump" aussuchen und sieht danach welchen "Trump" der Computer ausgewählt hat</p>
            <p style="font-size: medium;"> Danach kann man den Stat aussuchen mit welchen die Charakter gegeinander Kämpfen.</p>
        </li>
        <br>
        <li>
            <br>
            <img src="../static/images-portfolio/Top_Trumps_3.jpg">
            <p style="font-size: medium;">Nachdem aussuchen der Stats gewinnt der "Trump" mit den höheren Stat</p>
        </li>
        <li>
            <br>
            <img src="../static/images-portfolio/Top_Trumps_4.jpg">
            <p style="font-size: medium;">Wenn man im Menu view wählt kann man sich alle vorhanden "Trumps" und deren stats ansehen</p>
        </li>
        <li>
            <br>
            <img src="../static/images-portfolio/Top_Trumps_5.jpg">
            <br><img src="../static/images-portfolio/Top_Trumps_6.jpg">
            <p style="font-size: medium;">Mit "Add Trumps" kann man sich seinen eigenen "Trump" erstellen</p>
        </li>
    </ol>

    
    <br><a href="https://github.com/Xelon6/100_Days_Python/tree/main/Day%2041-50/Day%2047"  target="_blank" style="font-size: medium;">Github Link</a>

    <br><a href="/portfolio"style="font-size:medium;">Go back</a>
</div>
</body>
</html>
    """
    return page



app.run(host='0.0.0.0', port=81) # This line should ALWAYS come last. It's the line that turns on the Flask server.