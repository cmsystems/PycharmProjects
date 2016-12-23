__author__ = 'Thomas'
inchzucm = 2.54
eingabe = inchzucm
while eingabe != 0:
    print("Bitte geben sie einen inch wert ein")
    e = input()
    eingabe = float(e)
    print("Ergebnis: ", eingabe*inchzucm)