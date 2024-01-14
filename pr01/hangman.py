import random

# PARTIE 1 ===================================================================================
dictionnaire = [
    {
        "mot": "luzerne",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "jury",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "comete",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "competition",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "respirer",
        "type": "verbe",
        "temps": "infinitif"
    },
    {
        "mot": "cuisinier",
        "type": "verbe",
        "temps": "infinitif"
    },
    {
        "mot": "pneus",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "hippopotame",
        "type": "nom",
        "genre": "masculin"
    },
    {
        "mot": "pression",
        "type": "nom",
        "genre": "féminin"
    },
    {
        "mot": "collision",
        "type": "nom",
        "genre": "féminin"
    }
]

#Création d'une liste des noms féminim a partir des variables
liste_nom_fem = []
for dico in dictionnaire:
    if "genre" in dico.keys():
        if dico["genre"] == "féminin":
            liste_nom_fem.append(dico["mot"])
# PARTIE 2 ==================================================================================
print(liste_nom_fem)
#Initialisation des variables
liste_nom_fem_1 = list(set(liste_nom_fem))
lettre_deviner = []
nbs = 5
mot_deviner = random.choice(liste_nom_fem_1)
mot_deviner_montrer = len(mot_deviner) * '_'

#Début du code du mechanisme du jeu
#Boucle tant que pour continuer le jeux jusqu'à ce que le joueur gagne ou le nombre de vies est 0
while nbs != 0 and mot_deviner != mot_deviner_montrer:
    
    if len(lettre_deviner) > 0:
        print("Les lettres essayées a date sont: "+", ".join(lettre_deviner))
    lettre = input("Entrez une lettre: ")   #Entrée d'une lettre
    
    if lettre in lettre_deviner:    #Si la lettre a été déjà essayée par le joueur
        print("Vous avez déjà essayé cette lettre")
        print("=================================================")

    
    elif lettre in mot_deviner:     #Si la lettre est dans le mot à deviner
        if lettre not in lettre_deviner:
            lettre_deviner.append(lettre)
                                                 
    
        for indice,value in enumerate(mot_deviner):
            if value == lettre:
                mot_deviner_montrer = mot_deviner_montrer[:indice] + lettre + mot_deviner_montrer[indice + 1 :]
        print("Bon essai! Le mot est maintenant: ",mot_deviner_montrer)
        print("=================================================")
    

    else:                           #Si le mot à deviner ne contient pas la lettre choisit
       lettre_deviner.append(lettre)
       nbs = nbs - 1
       
       print("Mavais essai! Il vous reste ", nbs, "vies")
       print("==================================================")

if mot_deviner_montrer != mot_deviner:     #Si le joueur  perd
     print("Perdu :( Meilleur chance la prochaine fois!")
else:                                      #Si le joueur gange
    print("Bravo! Vous avez deviné le mot ",mot_deviner_montrer)
