
from organismeVivant import OrganismeVivant
from poisson import Poisson
from plante import Plante

# TODO: Implementer la classe Aquarium

class  Aquarium():
    
    contenuEnvironnement = []
    
    @property
    def json(self):
        
        dicitonnaireEspeces = {
                        "aquarium" : {
                            "poissons": [creature.JSON() for creature in self.contenuEnvironnement if type(creature) == Poisson],
                            "plantes": [creature.JSON() for creature in self.contenuEnvironnement if type(creature) == Plante]
                                    }
                            }
        return dicitonnaireEspeces
    
    
    def __add__(self,other):
        if other not in self.contenuEnvironnement:
            self.contenuEnvironnement.append(other)
        
    def __sub__(self,other):
        if other in self.contenuEnvironnement:
            self.contenuEnvironnement.remove(other)
        
    def __len__(self):
        return len(self.contenuEnvironnement)