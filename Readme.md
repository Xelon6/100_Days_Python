100 Days python Challenge
auf Replit.com


Things i learned:

Day4:

\33[31m everything after that in a print statement has a different color

Color	Value
Default	\33[0m
Black	\33[30m
Red	    \33[31m
Green	\33[32m
Yellow	\33[33m
Blue	\33[34m
Purple	\33[35m
Cyan	\33[36m
White	\33[37m

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

Day 37:

String Splicing 

mit index [0] kann man einzelnen Charakter in einem String lesen

wenn man 2 Argumenten getrennt von einem : nimmt kann man die Charakter x bis x lesen [0:6] --> vom start bis zum 6. Charakter

man kann aber auch ein 3. Argument benutzen [0:6:2] das dritte argument gibt an wie das ganze gelesen werden soll

mit 2 wird nur jeder 2. Charakter ausgegeben mit [::-1] wird der ganze String rückwärts ausgegeben

mit split() können wir einen String in eine liste verwandeln bei jedem Leerzeichen wird ein neues Objekt gesplittet:
"Hello There how are you" --> ["Hello", "There", "how", "are", "you"]