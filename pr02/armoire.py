from consts import *
import random
from preprocessing import *
# TODO: Créer la classe Vetement avec les paramètres estDIY, prixAchat, prixVente, profit, couleur1, couleur2, style, typeObj
class Vetement:
    def __init__(self, nom, estDIY, prixAchat, prixVente, couleur1, couleur2, style, typeObj, balance):
        self.nom = nom
        self.prixAchat = prixAchat
        self.prixVente = prixVente
        self.couleur = [couleur1, couleur2]
        self.style = style
        self.typeObj = typeObj
        self.estDIY = True if estDIY == 'Yes' else  False

        if balance != self.prixVente - self.prixAchat :
            self.balance = self.prixVente - self.prixAchat
            print("Erreur de commptabilité")
        else:
            self.balance = balance

# TODO: Créer la classe Armoire avec les paramètres dataframe et les méthodes de classes remplirArmoire, calculerValeurTotale, ajouterVetement, enleverVetement, obtenirNombreDIY, filtrerParTypeEtCouleur and creerHabitParStyle
class Armoire:
    listeVetements = []

        
    @classmethod
    def remplirArmoire(cls, dataframe):
        for vetement in dataframe.itertuples():
            objectVetement = Vetement(vetement.Name, vetement.DIY, vetement.Buy_Price, vetement.Sell_Price, vetement.Color_1, vetement.Color_2, vetement.Style, vetement.type,  vetement.Balance)
            cls.listeVetements.append(objectVetement)
        return cls.listeVetements 

    @classmethod
    def calculerValeurTotale(cls):
        somme = 0
        for Vetement in cls.listeVetements:
            somme += Vetement.prixVente
        return somme
        


    @classmethod
    def ajouterVetement(cls, other):
        cls.listeVetements.append(other)
    
    @classmethod
    def enleverVetement(cls, nom, type):
        listeVetementsCopy = cls.listeVetements.copy()
        for Vetement in listeVetementsCopy :
            if Vetement.nom == nom and Vetement.typeObj == type:
                cls.listeVetements.remove(Vetement)      

    @classmethod
    def obtenirNombreDIY(cls):
        c = 0
        for Vetement in cls.listeVetements:
            if Vetement.estDIY == True:
                c += 1
        return c
    

    @classmethod
    def filtrerParTypeEtCouleur(cls, type, couleur):
        return [vetement for vetement in cls.listeVetements if (vetement.couleur[0] == couleur or vetement.couleur[1] == couleur) and vetement.typeObj == type]
    
    @classmethod
    def creerHabitParStyle(cls, style):
        listBot = [vetement for vetement in cls.listeVetements if (vetement.typeObj ==  NOM_TYPE_BAS and  vetement.style == style)  ]
        listTop = [vetement for vetement in cls.listeVetements if (vetement.typeObj ==  NOM_TYPE_HAUT and vetement.style == style)  ]
        listChaussures = [vetement for vetement in cls.listeVetements if (vetement.typeObj ==  NOM_TYPE_CHAUSSURES and vetement.style == style) ] 
        return random.choice(listBot), random.choice(listTop), random.choice(listChaussures)
    




    



