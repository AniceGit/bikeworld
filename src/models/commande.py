from utilisateur import Utilisateur
from adresse import Adresse
from produit_commande import ProduitCommande


class Commande:
    liste_produit_commande = []
    def __init__(self, id: int, date_commande: str, etat: str, prix_total: float, frais_livraison: float,
                 liste_produit_commande: list[ProduitCommande], utilisateur: Utilisateur, adresse: Adresse) -> None:
        self.id = id
        self.date_commande = date_commande
        self.etat = etat
        self.prix_total = prix_total
        self.frais_livraison = frais_livraison
        self.liste_produit_commande = liste_produit_commande
        self.utilisateur = utilisateur
        self.adresse = adresse
