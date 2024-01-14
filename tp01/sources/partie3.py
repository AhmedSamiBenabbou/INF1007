# PARTIE 3: Fonction avancées de la calculatrice

def operationListe(listeA, listeB):
    # TODO: C_i  est égal à 3 * A_i 0 2 * B_i, le tout divisé par 6
    # Si A et B ne sont pas de même taille, retourner None
    listeResultat = []
    # TODO: Ajouter code ici
    if len(listeA) != len(listeB):
        return None
    else:
        
        for i in range(len(listeA)):
            listeResultat.append((3 * listeA[i] + 2 * listeB[i])/6) 

    return listeResultat 


def enleverDoublons(liste):
    # TODO: Enlever les nombres en double dans la liste
    # ex [1,2,1,5,3,2,1,4] -> [1,2,5,3,4]

    # TODO: Ajouter code ici
    return list(set(liste))
    #liste_valeur_unique = []
    #for element in liste:
    #    if element not in liste_valeur_unique:
    #        liste_valeur_unique.append(element)
    #
    #return liste_valeur_unique



def calculerPosVitesseAChaqueCapture(positionInit, vitesseInit, acceleration, nbCaptures, secondesEntreCaptures):
    # TODO: Calculer la vitesse d'un véhicule à chaque tic pour nbCaptures tics
    # TODO: Ajouter code ici
    historiquePosition = [positionInit]
    historiqueVitesse = [float(vitesseInit)]  ######verifier si on doit mettre le float ou pas

    for i in range(0,nbCaptures):
        historiquePosition.append(historiquePosition[-1] + historiqueVitesse[-1] * secondesEntreCaptures + ( 1/2 ) * acceleration * pow(secondesEntreCaptures, 2))
        historiqueVitesse.append(historiqueVitesse[-1] + acceleration * secondesEntreCaptures)
    

    return historiquePosition, historiqueVitesse


# PAS TOUCHER
if __name__ == "__main__":
    print("Exécutez le fichier calculatrice.py ou le fichier tests.py!")