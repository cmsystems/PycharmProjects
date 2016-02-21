__author__ = 'Thomas'
# Definition der klasse fahrzeug
class Fahrzeug:
    def __init__(self, bez, ge):        #Konstruktormethode
        self.bezeichnung = bez
        self.geschwindigkeit = ge
    def __str__(self):                  #Ausgabe Methode
        return self.bezeichnung + " "\
            + str(self.geschwindigkeit) + "km/h"
    def __repr__(self):                 #Info-Methode
        return "Objekt" + self.bezeichnung \
               + "der klassee Fahrzeug"

#Obejekte der Klasse Fahrzeug erzeugen
opel = Fahrzeug("Opel Admiral", 40)
volvo = Fahrzeug("Volvo Amazon", 45)

#Objekte Ausgeben
print(opel)
print(volvo)

# Informationen zu Objekt
print(repr(opel))
print(repr(volvo))