import random
import numpy as np
from consts import COULEUR_VIDE, LARGEUR_GRILLE, HAUTEUR_GRILLE, PIECES, NOMBRE_MAX_ROTATIONS
from typing import Dict, List, Tuple, NoReturn

# NE PAS TOUCHER À CETTE SECTION
def obtenirPositionsPiece(baseShape, rotation, shapePosX, shapePosY):
    positions = []

    baseShape = faireTournerPiece(baseShape, rotation)

    for i, row in enumerate(baseShape):
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shapePosX + j, shapePosY + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 2)

    return positions


def estPositionValide(baseShape, rotation, shapePosX, shapePosY, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == [0, 0, 0]] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = obtenirPositionsPiece(baseShape, rotation, shapePosX, shapePosY)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] >= 0:
                return False

    return True


def tournerTableau90Droite(tableau : List[List]) -> List:
    # in: tableau
    #     un tableau 2D

    # out: le tableau tourné de 90 degrés vers la droite

    # ex:
    # in: [[1, 2], [3, 4]]
    # out: [[4, 1], [2, 3]]

    npArray = np.array(tableau)
    npArray90Deg = np.rot90(npArray, axes=(1, 0))

    return npArray90Deg.tolist()



# TODO =============================================

# TODO: Initialiser la grille de jeu avec la valeur de la couleur par défaut
def initialiserGrille() -> List[List]:
    # in : rien

    # out: une grille vide contenant la couleur par défaut

    return None


# TODO: Remplir la grille avec les pièces déjà placées, utiliser la fonction initialiserGrille()
def remplirGrille(positionsConfirmees: List[Dict]) -> List[List]:
    # in: positionsConfirmées
    #     représente les cases déjà remplies et leur couleurs, sous la forme d'une liste de dictionnaires
    #     ex:
    #     [{"ligne": 19, "colonne": 5, "couleur": [0, 255, 0]}, {"ligne": 19, "colonne": 6, "couleur": [255, 0, 0]}]

    # out: une grille contenant les couleurs associées aux positions confirmées
    #      ex: [[(0,0,0), ...], [(0,0,0), ...], ...[(255,0,0), (255,255,0), ...]]

    return None


# TODO: Retourner une pièce aléatoire de la liste des pièces PIECES
def obtenirPieceAleatoire() -> Dict:
    # in: rien

    # out: un dictionnaire comprenant les informations d'une pièce aléatoire

    return None


# TODO: Utiliser la fonction 'tournerTableau90Droite' pour obtenir la pièce tournée rotation nombre de fois
def faireTournerPiece(piece: List[List], rotation: int) -> List[List]:
    # in: piece
    #     un tableau 2d représentant la forme de la pièce
    #     ex :    [['.', '0', '0'],
    #              ['0', '0', '.']]

    # in: rotation
    #     un entier entre -NOMBRE_MAX_ROTATIONS et NOMBRE_MAX_ROTATIONS représentant la rotation de la pièce

    # out: un tableau 2d représentant la pièce tournée rotations nombre de fois
    #      ex:    [['0','.'],
    #              ['0','0'],
    #              ['.','0']]

    return None


# TODO: Vérifier si la partie est perdue (si une position confirmée est à la première ligne de la grille)
def estPartiePerdue(positionsConfirmees: List[Dict]) -> bool:
    # in: positionsConfirmees
    #     représente les cases déjà remplies et leur couleurs, sous la forme d'une liste de dictionnaires
    #     ex:
    #     [{"ligne": 19, "colonne": 5, "couleur": (0, 255, 0)}, {"ligne": 19, "colonne": 6, "couleur": (255, 0, 0)}]

    # out : valeur booléenne qui indique si on a perdu (vrai si la partie est perdue, faux sinon)

    return True


# TODO: Enlever les lignes complétées des positionsConfirmées
def enleverLignesPleines(grille: List[List], positionsConfirmees: List[Dict]) -> Tuple[int, List[Dict]]:
    # in: grille
    #     la grille de jeu contenant les couleurs de toutes les pièces (placées et non placées)

    # in: positionsConfirmees
    #     représente les cases déjà remplies et leur couleurs, sous la forme d'une liste de dictionnaires
    #     ex:
    #     [{"ligne": 19, "colonne": 5, "couleur": (0, 255, 0)}, {"ligne": 19, "colonne": 6, "couleur": (255, 0, 0)}]

    # out: Le score correspondant aux nombres de lignes complétées * 10

    # out: Une liste des positionsConfirmees SANS les positions qui faisaient parties de lignes complétées
    #      (Il ne faut pas non plus oublier de décaler les positions des lignes qui restent!)


    return 0, None


# TODO: Obtenir le score maximal de toutes les parties précédentes. Si aucun meilleur score, retourner 0
def obtenirMeilleurDernierScore() -> int:
    # in: rien

    # out: un entier représentant le meilleur score obtenu à travers toutes les parties précédentes


    return 0


# TODO: Sauvegarder le nouveau score s'il n'est pas égal à 0
def sauvegarderNouveauScore(nouveauScore) -> NoReturn:
    # in: nouveauScore: Un entier représentant le score obtenu à la dernière partie jouée

    # out: rien
    pass



