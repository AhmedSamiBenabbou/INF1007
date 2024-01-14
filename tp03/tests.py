from organismeVivant import OrganismeVivant
from poisson import Poisson
from plante import Plante
from aquarium import Aquarium
import numpy as np
from consts import *

# TODO: tester les méthodes de classe:

def testOrganismeVivant(facteur1, facteur2):
    # TODO: on veut tester la fonction scale
    OrganismeVivant.scaleOrganisme(facteur1)
    
    if (OrganismeVivant.matricTransfo != np.array([[facteur1,0,0],[0,facteur1,0],[0,0,facteur1]])).all():
        return False
    else:
        
        OrganismeVivant.scaleOrganisme(facteur2)
        
        if (OrganismeVivant.matricTransfo != np.array([[facteur1*facteur2,0,0],[0,facteur1*facteur2,0],[0,0,facteur1*facteur2]])).all():
            return False
        
        return True

def testPoisson(poisson1: Poisson,poisson2: Poisson):
    # TODO: on veut tester l'égalité
    Estegal = poisson1 == poisson2

    for attribut in ["type","nom","profondeurMin","profondeurMax","vitesse"]:
        if getattr(poisson2,attribut) != getattr(poisson1,attribut):
            if Estegal:
                return False
            return True
        
    if not Estegal:
        return False
    return True

def testPlante(plante1: Plante,plante2: Plante):
    # TODO: on veut tester l'égalité
    Estegal = plante1 == plante2

    for attribut in ["type","nom","profondeurMin","profondeurMax","estMaison"]:
        if getattr(plante1,attribut) != getattr(plante2,attribut):
            if Estegal:
                return False
            return True
        
    if not Estegal:
        return False
    return True

def testsAquarium(creature):
    # TODO: on veut tester l'addition, la soustraction et la fonction qui retourne la taille
    aquariumTest = Aquarium()
    
    aquariumTest + creature
    
    
    if creature not in aquariumTest.contenuEnvironnement:
        return False#, 1
    
    
    if len(aquariumTest.contenuEnvironnement) == 1:
        aquariumTest + creature
        if len(aquariumTest.contenuEnvironnement) != 1:
            return False#, 3 
    else:
        return False#, 2
    
    
    aquariumTest - creature
    
    if creature in aquariumTest.contenuEnvironnement:
        return False#, 4
        
    return True
        
    
    

if __name__ == "__main__":
    
    facteur1, facteur2, facteur3 = 10, 21, -5
    
    def EstOrganismeVivant():
        if testOrganismeVivant(facteur1,facteur2) and testOrganismeVivant(facteur1, facteur3):
            return True
        else:
            return False
    
    poissonTest1 = Poisson(NOM_POISSON_CARDINAL,10,15,22)
    poissonTest2 = Poisson(NOM_POISSON_CARDINAL,10,20,22)
    poissonTest3 = Poisson(NOM_POISSON_CORAIL,10,20,22)
    poissonTest4 = Poisson(NOM_POISSON_CARDINAL,10,15,25)
    poissonTest5 = Poisson(NOM_POISSON_CARDINAL,8,20,22)
    
    planteTest1 = Plante(NOM_PLANTE_CABBAGE,50,78,True)
    planteTest2 = Plante(NOM_PLANTE_CABBAGE,50,78,True)
    planteTest3 = Plante(NOM_PLANTE_PIQUANTE,50,78,True)
    planteTest4 = Plante(NOM_PLANTE_CABBAGE,50,78,False)
    planteTest5 = Plante(NOM_PLANTE_CABBAGE,50,79,True)
    
    def EstTestPoisson():
        if testPoisson(poissonTest1,poissonTest2) and testPoisson(poissonTest2,poissonTest3) and testPoisson(poissonTest2,poissonTest4) and testPoisson(poissonTest2,poissonTest5):
            return True
        return False

    def EsttestPlante():
        if testPlante(planteTest1,planteTest2) and testPlante(planteTest2,planteTest3) and testPlante(planteTest2,planteTest4) and testPlante(planteTest2,planteTest5):
            return True
        else:
            return False
        
    def EsttestAquarium():
        if testsAquarium(planteTest1) != True or testsAquarium(poissonTest1) != True:
            return False
        return True
            
        
    # TODO: Exécuter les tests et afficher les résultats
    if EstOrganismeVivant():
        print("ORGANISME_VIVANT: TEST REUSSI")
    else:
        print("ORGANISME_VIVANT: Test échoué")
        
    if EstTestPoisson():
        print("POISSON: TEST REUSSI")
    else:
        print("POISSON: Test échoué")
          
    if EsttestPlante():
        print("PLANTE: TEST REUSSI")
    else:
        print("PLANTE: Test échoué")
        
    if EsttestAquarium():
        print("AQUARIUM: TEST REUSSI")
    else:
        print("AQUARIUM: Test échoué")
        
