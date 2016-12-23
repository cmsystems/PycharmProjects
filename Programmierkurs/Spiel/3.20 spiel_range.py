__author__ = 'Thomas'
import random
random.seed()

#Werte und Berechnung
a = random.randint(1, 10)
b= random.randint(1, 10)
c = a + b
print("Die Aufgabe:",a, "+", b)

#Schleife mit for
for versuch in range(1, 10):
    #Eingabe
    print("Bitte eine Zahl eingeben: ")
    z = input()
    zahl = int(z)
    #Verzweigung
    if zahl == c:
        print(zahl, "ist richtig!")
        #Abbruch der Schleife
        break
    else:
        print("Die Zahl ist falsch")
        print("Anzahl Versuche: ", versuch)