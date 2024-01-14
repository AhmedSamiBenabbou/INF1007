import numpy as np
from consts import TYPE_ORGANISME
import abc
from abc import ABC,abstractproperty

# TODO: Implementer la classe OrganismeVivant
class OrganismeVivant(ABC):
    
    def __init__(self, nom: str, profondeurMin: int, profondeurMax: int) -> None:
        
        self.nom = nom
        self.profondeurMin = profondeurMin
        self.profondeurMax = profondeurMax if (profondeurMax - profondeurMin) >= 10 else profondeurMin + 10
        
        
    type = TYPE_ORGANISME
    matricTransfo = np.identity(3)


    @abstractproperty
    def JSON(self):
        ContenueObjet = {"nom": self.nom, "type" : self.type, "profondeurMin": self.profondeurMin, "profondeurMax": self.profondeurMax, "transformation": self.matricTransfo.tolist()}
        return ContenueObjet
    
    @classmethod
    def scaleOrganisme(cls, facteur: float):
        matriceScale = np.identity(3)*facteur
        cls.matricTransfo = np.dot(matriceScale,cls.matricTransfo)



