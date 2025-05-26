class Panier:

    def __init__(
        self, date_panier: str, prix_total: float, liste_produits_quantite: list[dict]
    ) -> None:
        """Instanciation d'un Panier

        Args:
            date_panier (str): date de la mise au panier
            prix_total (float): prix total de la commande
            liste_produits_quantite (list[dict]): liste des produits et leur quantité dans le panier
        """
        self.date_panier = date_panier
        self.prix_total = prix_total
        self.liste_produits_quantite = (
            liste_produits_quantite if liste_produits_quantite else []
        )
