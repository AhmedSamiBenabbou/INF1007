import pandas as pd
from consts import *
from armoire import *

if __name__ == "__main__":
    # TODO: Lire le dataframe de la partie 1 contenu dans CHEMIN_DF_COMPLET
    dataframe = pd.read_csv(CHEMIN_DF_COMPLET)

    # TODO: Créer un objet armoire à partir du dataframe
    Armoire.remplirArmoire(dataframe)
    
    # TODO: Créer un nouveau haut
    monTShirt = Vetement("EveryDay TShirt", "No", 150, 100, "Black", "Red", "Simple", NOM_TYPE_HAUT, -50 )
    
    # TODO: Ajouter le nouveau haut à armoire
    Armoire.ajouterVetement(monTShirt)
   
    # TODO: Enlever le bas avec le nom "animal-stripes skirt"
    Armoire.enleverVetement("animal-stripes skirt", NOM_TYPE_BAS)
    
    # TODO: Afficher la valeur totale de l'armoire
    print(f"NOMBRE TOTAL d'Armoire = {Armoire.calculerValeurTotale()} BELLS")
    
    # TODO: Afficher le nom de toutes les chaussures de couleur 'Blue'
    print([object.nom for object in Armoire.filtrerParTypeEtCouleur(NOM_TYPE_CHAUSSURES, "Blue")])
    
    # TODO: Afficher le nombre de vêtements qui sont DIY
    print(f"NOMBRE DE DIYs dans Armoire = {Armoire.obtenirNombreDIY()}")

    # TODO: Générer un habit avec le style 'Cool'
    bot, top, chaussures = Armoire.creerHabitParStyle("Cool")
    print(f"HABIT COOL ALERATOIRE = {bot.nom} + {top.nom} + {chaussures.nom}")

    # TODO: Générer un habit avec le style 'Cute'
    bot, top, chaussures = Armoire.creerHabitParStyle("Cute")
    print(f"HABIT CUTE ALERATOIRE = {bot.nom} + {top.nom} + {chaussures.nom}")

