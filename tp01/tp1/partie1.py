# PARTIE 1: Fonctions de base de la calculatrice

def additionner(a, b):
    # TODO: calculer somme de a et b
    somme = a + b

    return somme

def soustraire(a, b):
    # TODO: calculer différence entre a et b
    difference = a - b

    return difference

def multiplier(a, b):
    # TODO: calculer produit entre a et b
    produit = a * b

    return produit

def diviserAvecReste(a, b):
    # TODO: calculer quotient (ex: 5 / 2 = 2.5)
    quotient = a / b 
    # TODO: calculer reste ( ex: 5 / 2 reste 1)
    reste = a % 2 

    return quotient, reste


# PAS TOUCHER
if __name__ == "__main__":
    print("Exécutez le fichier calculatrice.py ou le fichier tests.py!")
