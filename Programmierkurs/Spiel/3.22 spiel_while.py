__author__ = 'Thomas'
#Zufalls generator
import random
random.seed()

#Werte Berechnung
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print("Die Aufgabe: ", a,"+ ", b)
#Schleife initialisieren
zahl = c +1

#Anzahl initialisieren
versuch = 0

#Schleife mit while
while zahl != c:
    #Anzahl versuche
    versuch = versuch +1

    #Eingabe mit Umwandlung
    print("Bitte geben Sie eine Zahl ein:")
    z = input()
    zahl = int(z)

    #verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
    else:
        print(zahl, "ist falsch")

#Anzahl ausgeben
print("Ergebnis: ", c)
print("Anzahl Versuche: ", versuch)
