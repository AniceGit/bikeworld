from typing import List
from adresse import Adresse

class Utilisateur:
    def __init__(self, id:int, nom:str, prenom:str, email:str, mdp:str, tel:str) -> None:
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mdp = mdp
        self.tel = tel
        self.liste_adresse:List[Adresse] = None
