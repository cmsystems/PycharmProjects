 # coding: latin-1

#Bruttogehalt einlesen
print("Bitte geben Sie Ihr monatliches Bruttogehalt ein:")
b = input()
brutto = int(b)

#Familienstand einlesen
print("Bitte geben Sie 1 für verheiratet oder 0  für ledig ein")
f = input()
familienstand = int(f)

#Steuersatz berechnen
if (brutto > 4000) and (familienstand == 1):
    s = 26
elif (brutto > 400) and (familienstand == 0):
    s = 22
elif (brutto <= 4000) and (familienstand == 1):
    s = 22
else:
    s = 18
steuersatz = int(s)

#Berechnung und Ausgabe der Steuern
steuerbetrag = ((brutto/100)* steuersatz)

print("Es ergibt sich ein monatlicher Steuersatz von: ",steuerbetrag)