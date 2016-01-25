__author__ = 'Thomas'
print("Bitte geben Sie ihr gehalt ein: ")
a = input()
gehalt = int(a)
def steuer(gehalt):
    if gehalt > 2500:
        steuersatz = 0.22
        return steuersatz
    else:
        steuersatz = 0.18
        return steuersatz

print("Der Steuerbetrag ist: ", gehalt*steuer(gehalt))
