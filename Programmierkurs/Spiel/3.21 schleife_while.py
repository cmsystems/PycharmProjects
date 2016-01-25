__author__ = 'Thomas'
#Zufallsgenerator
import random
random.seed()

#Initialisierung
summe = 0

#while schleife
while summe < 30:
    zzahl = random.randint(1, 8)
    summe = summe + zzahl
    print("Zahl:", zzahl, "Summe:", summe)