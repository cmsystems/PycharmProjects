__author__ = 'Thomas'
#Definition der klasse Fahrzeug
class Fahrzeug:
    geschwindigkeit = 0         #Eigenschaft
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    def ausgabe(self):
        print("Geschwindigkeit: ", self.geschwindigkeit)

# Objekte der KLasse Fahrzeug erzeugen
opel = Fahrzeug()
volvo = Fahrzeug()

#Objektmethoden
volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()