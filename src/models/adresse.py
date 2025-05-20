class Adresse:
    def __init__(self, id:int, numero:int, type_voie:str, nom_voie:str, code_postal:int, ville:str, pays:str) -> None:
        self.id = id
        self.numero = numero
        self.type_voie = type_voie
        self.nom_voie = nom_voie
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays