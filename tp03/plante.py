from organismeVivant import OrganismeVivant
from consts import TYPE_PLANTE
import numpy as np

# TODO: Implementer la classe Plante

class Plante(OrganismeVivant):
    
    def __init__(self, nom: str, profondeurMin: int, profondeurMax: int, estMaison: bool) -> None:
        super().__init__(nom, profondeurMin, profondeurMax)
        self.estMaison = estMaison
        
    type = TYPE_PLANTE
    matriceTransfo = np.identity(3) #super().matriceTransfo ???
    
    
    def JSON(self):
        dicitonnaire = super().JSON
        dicitonnaire["estMaison"] = self.estMaison
        return dicitonnaire

    
    def __eq__(self,other):
        if self.type == other.type:
            #for attribut in self.JSON().keys():
                if self.JSON() != other.JSON():
                    return False
                else:
                    return True
        else:
            return False
        
            