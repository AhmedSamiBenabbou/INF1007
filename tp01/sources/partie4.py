## PARTIE BONUS - PETIT DÉFI

def rotationListe(liste, rotation, estVersDroite):
    # TODO: Écrire la fonction qui fait tourner les éléments d'un liste
    # EX liste en entrée = [1, 2, 3, 4, 5], rotation = 3 et estVersDroite = vrai
    # reponse = [3, 4, 5, 1, 2]
    #EX liste en entrée = [1, 2, 3, 4, 5], rotation = 2 et estVersDroite = vrai
    # reponse = [4,5,1,2,3]
    # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    #EX liste en entrée = [1, 2, 3, 4, 5], rotation = 2 et estVersDroite != vrai
    # reponse = [3,4,5,1,2]
    #EX liste en entrée = [1, 2, 3, 4, 5], rotation = 3 et estVersDroite != vrai
    # reponse = [4,5,1,2,3]

    # TODO: Ajouter code ici
    taille_liste = len(liste)
    changement_de_position = rotation % taille_liste
    liste.extend(liste) 

    if estVersDroite == False:
        indice_commencement = changement_de_position
        nouvelle_liste = liste[indice_commencement : indice_commencement+taille_liste]

    else:
        indice_commencement = taille_liste - changement_de_position
        nouvelle_liste = liste[indice_commencement : indice_commencement+taille_liste]
    return nouvelle_liste
# PAS TOUCHER
if __name__ == "__main__":
    print("Exécutez le fichier calculatrice.py ou le fichier tests.py!")