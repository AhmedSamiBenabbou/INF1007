from armoire import *
import pandas as pd
from consts import *
import csv
from typing import List, NoReturn, Tuple

# TODO: Tester la fonction remplirArmoire de la classe Armoire
def testRemplirArmoire():

    dataframe = pd.read_csv(CHEMIN_DF_COMPLET)
    with open(CHEMIN_DF_COMPLET, "r") as f:
        fichier = list(csv.reader(f, delimiter = ","))
        del fichier[0]
    Armoire.remplirArmoire(dataframe)
    if len(fichier)  != len(Armoire.listeVetements):
        return False
    return True

# TODO: Tester la fonction calculerValeurTotale de la classe Armoire
def testCalculerValeurTotale():

    with open(CHEMIN_DF_COMPLET, "r") as f:
        fichier = list(csv.reader(f, delimiter = ","))
        del fichier[0]
    somme = 0
    for obj in fichier:
            somme += int(obj[4])
    if Armoire.calculerValeurTotale() != somme:
        return False
    return True

# TODO: Tester la fonction ajouterVetement de la classe Armoire
def testAjouterVetement(): 

    Object = Vetement("nom", "No", 0, 0, "Color 1", "Color 1", "Style", NOM_TYPE_HAUT, 0 )
    Armoire.ajouterVetement(Object)
    if Object not in Armoire.listeVetements:
        return False
    return True
     

# TODO: Tester la fonction enleverVetement de la classe Armoire
def testEnleverVetement():

    Armoire.enleverVetement("animal-stripes skirt", NOM_TYPE_BAS)
    for vetement in Armoire.listeVetements:
        if (vetement.nom == "animal-stripes skirt" and vetement.typeObj == NOM_TYPE_BAS):
            return False
        return True


# TODO: Tester la fonction obtenirNombreDIY de la classe Armoire
def testObtenirNombreDIY():
    with open(CHEMIN_DF_COMPLET, "r") as f:
        fichier = list(csv.reader(f, delimiter = ","))
        del fichier[0]
    nbsDIY = 0
    for obj in fichier:
            if obj[2] == "Yes":
                nbsDIY += 1
    if Armoire.obtenirNombreDIY() != nbsDIY:
        return False
    return True

# TODO: Tester la fonction filtrerParTypeEtCouleur de la classe Armoire
def testFiltrerParTypeEtCouleur():
    dataframe = pd.read_csv(CHEMIN_DF_COMPLET)
    Armoire.remplirArmoire(dataframe)
    listObjetToList = []
    cpt = 0
    
    with open(CHEMIN_DF_COMPLET, "r") as f:
        fichier = list(csv.reader(f, delimiter = ","))
        del fichier[0]

    listDataframefiltrer = Armoire.filtrerParTypeEtCouleur(NOM_TYPE_CHAUSSURES, "Blue")
    listFiltrer = [vetement for vetement in fichier if vetement[8] == NOM_TYPE_CHAUSSURES and (vetement[5] == "Blue" or vetement[6] == "Blue")]
    listObjetToList = [[ObjVetement.nom, ObjVetement.estDIY, ObjVetement.prixAchat, ObjVetement.prixVente, ObjVetement.couleur[0], ObjVetement.couleur[1], ObjVetement.style, ObjVetement.typeObj,  ObjVetement.balance] for ObjVetement in listDataframefiltrer]

    for subList, sublistDataframe in zip(listFiltrer, listObjetToList):
        if subList[1] == sublistDataframe[0]:
            cpt += 1
    if  cpt == len(listFiltrer):
        return True
    return False
    
# TODO: Tester la fonction creerHabitParStyle de la classe Armoire
def testCreerHabitParStyle(): 
    dataframe = pd.read_csv(CHEMIN_DF_COMPLET)
    Armoire.remplirArmoire(dataframe)
    bot, top, Chaussures = Armoire.creerHabitParStyle('Cute')
 
    with open(CHEMIN_DF_COMPLET, "r") as f:
        fichier = list(csv.reader(f, delimiter = ","))
        del fichier[0]
    return any(bot.nom and top.nom and Chaussures.nom for sublist in fichier )

def afficherResulatat(f):
        if  f() == True:
            print(f"la fonction {f.__name__} fonctionne bien :)")
        else:
            print(f"la fonction {f.__name__} ne fonctionne pas :/")


if __name__ == "__main__":
    # TODO: Exécuter les tests et afficher les résultats
    afficherResulatat(testRemplirArmoire)
    afficherResulatat(testCalculerValeurTotale)
    afficherResulatat(testEnleverVetement)
    afficherResulatat(testObtenirNombreDIY)
    afficherResulatat(testFiltrerParTypeEtCouleur)
    afficherResulatat(testCreerHabitParStyle)
