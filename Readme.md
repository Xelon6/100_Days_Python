100 Days python Challenge
auf Replit.com


Things i learned:

Day4:

\33[31m everything after that in a print statement has a different color

Color	Value
Default	0
Black	30
Red	    31
Green	32
Yellow	33
Blue	34
Purple	35
Cyan	36
White	37

\33[(colorcode)m

Day 10:

floats auf 2 dezimal stellen begrenzen mit:

variable = round(answer,2)

oder 

variable = "{:.2f}".format(variable)

Day 17:

while loop break, exit(), continue

mit break brechen wir aus dem loop aus und der nächste command außerhalb des loops wird executed

mit exit() schließen wir das komplette script also werden alle commands nach exit () nicht ausgeführt

mit continue starten wir einen loop von vorne und alle commands nach continue werden ignoriert

Day 29:
print secrets

ich kann festlegen was , in str machen
print("Hey","wie gehts")
hier macht das , automatisch einen abstand
aber mit sep (seperator) kann ich was anderes festlengen
print("Hey","wie gehts",sep=0) --> Hey0wie gehts

mit end= kann ich festlegen was am ende eines strings passiert und somit auch
die automatische newline funktion deaktivieren um mit mehrern
print statements in einer zeile was zu schreiben