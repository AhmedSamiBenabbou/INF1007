from organismeVivant import OrganismeVivant
from consts import TYPE_POISSON

# TODO: Implementer la classe Poisson


class Poisson(OrganismeVivant):
    
    def __init__(self, nom: str, profondeurMin: int, profondeurMax: int, vitesse: float) -> None:
        super().__init__(nom, profondeurMin, profondeurMax)
        self.vitesse = vitesse
    
    type = TYPE_POISSON
    
    
    def JSON(self):
        dicitonnaire = super().JSON
        dicitonnaire["vitesse"] = self.vitesse
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



