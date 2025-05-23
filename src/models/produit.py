class Produit:
    def __init__(
        self,
        id: int,
        nom: str,
        description: str,
        spec_tech: str,
        couleur: str,
        image: str,
        prix: float,
        stock: int,
        ventes: int,
    ) -> None:
        """Instanciation d'un Produit

        Args:
            id (int): identifiant du produit
            nom (str): Nom du produit
            description (str): Description du produit
            spec_tech (str): Specifications technioques du produit
            couleur (str): Couleur
            image (str): URI de l'image du produit
            prix (float): prix unitaire du produit
            stock (int): Stock disponible du produit
            ventes (int): Nombre de ventes totales du produit
        """
        self.id = id
        self.nom = nom
        self.description = description
        self.spec_tech = spec_tech
        self.couleur = couleur
        self.image = image
        self.prix = prix
        self.stock = stock
        self.ventes = ventes
