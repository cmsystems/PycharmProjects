__author__ = 'Thomas'
# coding: latin-1
#initialisierung
verhaeltnis = 381/150
inch = 0
a = inch + 1


while a > 0:
    #Einlesen der inch werte
    print("Bitte geben sie einen Inch Wert ein den sie in cm umwandeln moechten")
    i = input()
    inch = int(i)
    print(inch, "inch sind ", inch * verhaeltnis, "cm")
    if inch == 0:
        break