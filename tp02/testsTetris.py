from tetris_corrige.fonctions import faireTournerPiece, initialiserGrille
from fonctions import *
import json


def testInitialiserGrille(cheminFichier: str) -> bool:
    #TODO: Lire le fichier passé en paramètre, et comparer le résultat des tests avec le résultats de la fonction initialiserGrille

    return False


def testRemplirGrille(cheminFichier: str) -> bool:
    #TODO: Lire le fichier passé en paramètre, et comparer le résultat des tests avec le résultats de la fonction remplirGrille

    return False


def testFaireTournerPiece(cheminFichier: str) -> bool:
    #TODO: Lire le fichier passé en paramètre, et comparer le résultat des tests avec le résultats de la fonction faireTournerPiece

    return False


def testEstPartiePerdue(cheminFichier: str) -> bool:
    #TODO: Lire le fichier passé en paramètre, et comparer le résultat des tests avec le résultats de la fonction testEstPartiePerdue

    return False


def testEnleverLignesPleines(cheminFichier: str) -> bool:
    #TODO: Lire le fichier passé en paramètre, et comparer le résultat des tests avec le résultats de la fonction enleverLignesPleines

    return False


if __name__ == "__main__":
    # TODO: Remplacer les lignes suivantes et appeller les fonctions définies pour tester le fichier fonctions.py
    initialiserGrilleSucces = False
    remplirGrilleSucces = False
    faireTournerPieceSucces = False
    estPartiePerdueSucces = False
    enleverLignesPleinesSucces = False

    # Affichage des résultats
    if initialiserGrilleSucces:
        print("Tests initialiserGrille succès :)")
    else:
        print("Tests initialiserGrille échec :(")


    if remplirGrilleSucces:
        print("Tests remplirGrille succès :)")
    else:
        print("Tests remplirGrille échec :(")


    if faireTournerPieceSucces:
        print("Tests faireTournerPiece succès :)")
    else:
        print("Tests faireTournerPiece échec :(")


    if estPartiePerdueSucces:
        print("Tests estPartiePerdue succès :)")
    else:
        print("Tests estPartiePerdue échec :(")


    if enleverLignesPleinesSucces:
        print("Tests enleverLignesPleines succès :)")
    else:
        print("Tests enleverLignesPleines échec :(")