# #✅ 1. Zahlen von 1 bis 10 ausgeben
# #Schreibe ein Programm, das mit einer while-Schleife die Zahlen 1 bis 10 ausgibt.

# zahl = 1
# while zahl <= 10:   # true
#     print(zahl)
#     zahl = zahl + 1  # zahl += 1

# #✅ 2. Countdown
# #Lass einen Countdown von 10 bis 0 herunterzählen und danach „Start!“ ausgeben.

# count = 10
# while count >= 1:  # true
#     print(count)
#     count -= 1

#  ✅ 3. Gerade Zahlen
# Gib mit einer while-Schleife alle geraden Zahlen von 0 bis 50 aus.

# wert = 1

# while wert <= 50:
#     if wert % 2 == 0:
#         print(wert)
#     wert = wert + 1

# ✅ 4. Passwort abfragen
# Frage den Benutzer so lange nach einem Passwort, bis er „geheim“ eingibt.

# while True:
#     eingabe = input('Tippe dein Passwort: ')
#     if eingabe == 'geheim':
#         break


# print('Eingelogt')
# ✅ 5. Zahlen addieren
# Frage den Benutzer wiederholt nach Zahlen und addiere sie, bis er 0 eingibt. Danach soll die Summe ausgegeben werden.

# import random
# summe = 0

# while True:
#     zahl_summe = int(input('Ganze Zahl eingeben (Exit 0): '))
#     summe = summe + zahl_summe
#     if zahl_summe == 0:
#         break

# print(summe)  # endergebnis printen lassen!

# ✅ 6. Zufallszahl raten
# Lass eine zufällige Zahl zwischen 1 und 100 generieren. Der Nutzer soll raten, bis er richtig liegt. Gib Hinweise („zu groß/zu klein“).
import random

zufall_zahl = random.randint(1, 100)
print(zufall_zahl)

while True:
    zahl = int(input('Zufallzahl eingeben: '))
    if zahl < zufall_zahl:
        print('Zahl zu klein!')
    elif zahl > zufall_zahl:
        print('Zahl zu groß!')
    else:
        print(zufall_zahl, 'Richtig geraten!')
        break


# ✅ 7. Zeichen zählen
# Lasse den Benutzer einen Text eingeben und zähle die Zeichen, ohne len() zu benutzen (mit while).


# ✅ 8. Multiplikationstabelle
# Lass den Benutzer eine Zahl eingeben und gib mit einer while-Schleife die Multiplikationstabelle 1–10 aus.


# ✅ 9. Liste rückwärts ausgeben
# Gegeben ist eine Liste (z. B. [3,6,2,9]), gib sie mit while rückwärts aus.


# ✅ 10. Eingabe validieren
# Fordere den Benutzer auf, eine Zahl zwischen 1 und 5 einzugeben. Solange er etwas anderes schreibt, frag erneut.
