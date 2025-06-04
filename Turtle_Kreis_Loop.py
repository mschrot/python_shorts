import turtle             # Turtle-Modull


my_var = turtle.Turtle()  # Variable erstellen --> funktion zuweisen --> Zeichenstift


my_var.speed(100)         # Geschwindigkeit von Objekten festlegen
turtle.bgcolor('black')   # Hintergrundfarbe für App-Fenster


# For in Schleifen:
for zahl in range(240):   # Durchläufe von 0 bis 239
    my_var.color('aqua')  # Farbe
    my_var.circle(zahl)   # Radius um 1 > vergrößer pro Schleifendurchlauf
    my_var.left(5)        # Bewegungsrichtung leicht ändern pro Schleifendurchlauf 


turtle.done()             # Nach ablauf App-Fenster anlassen mit Endergebnis