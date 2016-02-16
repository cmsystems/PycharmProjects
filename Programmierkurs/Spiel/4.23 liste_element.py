__author__ = 'Thomas'
#Originalliste
fr =["Paris", "LYon", "MArseile", "Bordeaux"]
print("Original: ")
print(fr)

#Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt: ")
print(fr)

#Ersetzen eines Teilbereichs durch eine Liste
fr[1:3] = ["Nancy", "Metz", "Gap"]
#Ersetzen eines Teilbereiches
del fr[3:]
print("Teil entnommen: ")
print(fr)

#Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Sued"]
print("Element durch Liste ersetzt: ")
print(fr)

