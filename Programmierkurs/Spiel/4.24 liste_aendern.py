__author__ = 'Thomas'
#Originalliste
fr =["Paris", "LYon", "MArseile", "Bordeaux"]
print("Original: ")
print(fr)
#Einsetzen eines Elements
fr.insert(0, "Nantes")
print("Nach einsetzen: ")
print(fr)

#Sortieren der Elemente
fr.sort()
print("Nach sortieren: ")
print(fr)

#Umderehen der Liste
fr.reverse()
print("Nach umdrehen: ")
print(fr)

#Entfernen eines Elements
fr.remove("Nantes")
print("Nach entfernen eines Elements: ")
print(fr)

#Ein Element am ende hinzufuegen
fr.append("Paris")
print("Ein Element hinzufuegen:")
print(fr)

#Suchen bestimmter Elemente
print("Erste Position Paris: ", fr.index("Paris"))

