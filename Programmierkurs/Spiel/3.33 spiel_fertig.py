__author__ = 'Thomas'
# Zufalls generator
import random

random.seed()

# Anzahl aufgaben
anzahl = -1

while anzahl < 0 or anzahl > 10:
    try:
        print("Wieviele Aufgaben (1 - 10):")
        anzahl = int(input())
    except:
        continue

# Anzahl richtrige Ergebnisse
richtig = 0

for aufgabe in range(1, anzahl + 1):
    # operatorauswahl
    opzahl = random.randint(1, 4)

    # operatorauswahl
    if (opzahl == 1):
        a = random.randint(-10, 30)
        b = random.randint(-10, 30)
        op = "+"
        c = a + b
    elif (opzahl == 2):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        op = "-"
        c = a - b
    elif (opzahl == 3):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "*"
        c = a * b
    elif (opzahl == 4):
        c = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "/"
        a = c * b

    # Aufgabenstellung
    print("Aufgabe", aufgabe, "von", anzahl, ":", a, op, b)

    # Schleife mit 3 versuchen
    for versuch in range(1, 4):
        # Eingabe
        try:
            print("Bitte zahl eingeben:")
            zahl = int(input())
        except:
            # Falls Umwandlung nicht erfolgreich
            print("Sie haben keine Zahl eingegeben")
            # Schleife unmittelbar fortsetzen
            continue
        if zahl == c:
            print(zahl, "ist richtig")
            richtig = richtig + 1
            break
        else:
            print(zahl, "ist falsch")
    print("Richtig", richtig, "von", anzahl)
