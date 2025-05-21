class Adresse:
    def __init__(
        self,
        id: int,
        numero: str,
        type_voie: str,
        nom_voie: str,
        code_postal: str,
        ville: str,
        pays: str,
        defaut: int,
        id_utilisateur: int,
    ) -> None:
        """Instanciation d'une Adresse

        Args:
            id (int): identifiant de l'adresse (pk)
            numero (str): Numéro de rue
            type_voie (str): Type de voie
            nom_voie (str): Nom de la voie
            code_postal (str): Code postal
            ville (str): Ville
            pays (str): Pays
            defaut (int): Adresse par défaut de l'utilisateur
            id_utilisateur (int): identifiant utilisateur (fk)
        """
        self.id = id
        self.numero = numero
        self.type_voie = type_voie
        self.nom_voie = nom_voie
        self.code_postal = code_postal
        self.ville = ville
        self.pays = pays
        self.defaut = defaut
        self.id_utilisateur = id_utilisateur
