__author__ = 'Thomas'
# Definition der klasse fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):        #Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __gt__(self, other):            #Vergleichsmethode
        return self.geschwindigkeit > other.geschwindigkeit
    def __eq__(self, other):            #Vergleichsmethode
        return self.geschwindigkeit == other.geschwindigkeit
    def __sub__(self, other):
        return self.geschwindigkeit - other.geschwindigkeit

#Obejekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 60)
volvo = Fahrzeug("Volvo Amazon", 45)

#Objekte vergleichen
if opel > volvo:
    print("Opel ist schneller")
elif opel == volvo:
    print("Beide sind gleich schnell")
else:
    print("Volvo ist schneller")

#Objekte subtrahieren
diffrenz = opel - volvo
print("Geschwindigkeitsdifferenz: ", diffrenz, "km/h")