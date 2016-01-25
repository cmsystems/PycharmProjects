__author__ = 'Thomas'
 # coding: latin-1
def steuer(gehalt):
    if gehalt > 2500:
        steuersatz = 0.22
        print("Der Steuerbetrag ist: ", gehalt*steuersatz)
    else:
        steuersatz = 0.18
        print("Der Steuerbetrag ist: ", gehalt*steuersatz)
steuer(1800)
steuer(2200)
steuer(2500)
steuer(2900)