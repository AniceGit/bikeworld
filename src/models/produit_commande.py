from produit import Produit

class ProduitCommande:
    def __init__(self, id: int, quantite: int, prix: float, produit: Produit):
        self.id = id
        self.quantite = quantite
        self.prix = prix
        self.produit = produit

