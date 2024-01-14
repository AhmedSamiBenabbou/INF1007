# PAS TOUCHER À CE FICHIER
from partie1 import *
from partie2 import *
from partie3 import *
from partie4 import *

operations = {
    "add": {
        "func": additionner,
        "operands": {
            "a": float,
            "b": float
        }
    },
    "sub": {
        "func": soustraire,
        "operands": {
            "a": float,
            "b": float
        }
    },
    "mul": {
        "nom": "mul",
        "func": multiplier,
        "operands": {
            "a": float,
            "b": float
        }
    },
    "div": {
        "func": diviserAvecReste,
        "operands": {
            "a": float,
            "b": float
        }
    },
    "min": {
        "func": calculerMinutes,
        "operands": {
            "annees": int,
            "mois": int,
            "jours": int,
            "heures": int,
            "minutes": int,
            "secondes": int
        }
    },
    "arr": {
        "func": arrondir,
        "operands": {
            "nombre": int,
            "facteurArrondissement": int
        }
    },
    "nba": {
        "func": calculerNombreA,
        "operands": {
            "mot": str
        }
    },
    "op": {
        "func": operationListe,
        "operands": {
            "listeA": list,
            "listeB": list
        }
    },
    "doub": {
        "func": enleverDoublons,
        "operands": {
            "liste": list
        }
    },
    "car": {
        "func": calculerPosVitesseAChaqueCapture,
        "operands": {
            "positionInit": float,
            "vitesseInit": float,
            "acceleration": float,
            "nbCaptures": int,
            "secondesEntreCaptures": int
        }
    },
    "rot": {
        "func": rotationListe,
        "operands": {
            "liste": list,
            "rotation": int,
            "estVersDroite": bool
        }
    }
}

if __name__ == "__main__":
    # Affichage du message de bienvenue
    print("Bienvenue dans l'application =+= CALCULATRICE =+=")
    print("tip: pour entrer une liste, entrez des entiers séparés par des virgules (ex: 1,2,3,4)")
    print("Les opérations disponibles sont:")

    # Pour chaque élément de mon dictionnaire, j'affiche le nom et la valeur
    for name, op in operations.items():
        # func.__name__ représente la chaîne de caractères du nom de ma fonction
        print(f"\t- {name} : {op['func'].__name__}")

    # Lire ce que l'utilisateur veut faire
    op = input("Entrez le nom d'une opération ou Q pour quitter: ")

    while op not in 'Qq':
        # Si on ne comprends pas ce que l'utilisateur veut faire
        if op not in operations:
            print("Opération non reconnue")
            op = input("Entrez le nom d'une opération ou Q pour quitter: ")

        else:
            operandes = {}
            # On lit les opérandes dont on a besoin pour les demander à l'utilisateur
            for name, opType in operations[op]["operands"].items():
                operande = input(f"\t valeur de {name}: ")

                if opType != list:
                    # Caster dans le bon type
                    operandes[name] = opType(operande)
                else:
                    # Parser pour avoir la liste
                    operandes[name] = list(map(int, operande.split(',')))

            # Exécuter la fonction associée
            res = operations[op]["func"](**operandes)
            print(f"\tRÉSULTAT = {res}")

            # Demander la prochaine op
            op = input("Entrez le nom d'une opération ou Q pour quitter: ")




