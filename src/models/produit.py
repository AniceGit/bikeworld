class produit():
    def __init__(self, id:int, nom:str, description:str, spec_tech:str, couleur:str, image:str, prix:float, stock:int) -> None:
        '''
        Initialisation de la classe produit
        
        '''
        self.id = id
        self.nom = nom
        self.description = description
        self.spec_tech = spec_tech
        self.couleur = couleur
        self.image = image
        self.prix = prix
        self.stock = stock