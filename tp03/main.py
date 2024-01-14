import json

from consts import *
from poisson import Poisson
from plante import Plante
from aquarium import Aquarium



if __name__ == "__main__":
    # TODO: Instancier un aquarium
    aquarium = Aquarium()
    # TODO: Créer au moins 3 poissons
    poisson1 = Poisson(NOM_POISSON_CARDINAL,2,50,2.3)
    poisson2 = Poisson(NOM_POISSON_CORAIL,100,130,1.5)
    poisson3 = Poisson(NOM_POISSON_PUFF,8,43,10.5)
    
    # TODO: Ajouter les poissons à l'aquarium en les additionnant
    aquarium + poisson1
    aquarium + poisson2
    aquarium + poisson3
    
    # TODO: Enlever les poissons à l'aquarium en le soustrayant
    aquarium - poisson1
    aquarium - poisson2
    aquarium - poisson3
    
    # TODO: Créer au moins 2 plantes
    plante1 = Plante(NOM_PLANTE_CABBAGE,10,12,True)
    plante2 = Plante(NOM_PLANTE_PIQUANTE,0,15,False)
    
    # TODO: Ajouter les plantes à l'aquarium en les additionnant
    aquarium + plante1
    aquarium + plante2
    
    # TODO: Afficher taille aquarium:
    print(len(aquarium))
    
    # TODO: Écrire le contenu de l'aquarium dans le fichier OUT_FILE (format JSON)
    with open("OUT_FILE", "w", encoding="utf8") as fichierAquarium:
        json.dump(aquarium.json, fichierAquarium, indent=10)
