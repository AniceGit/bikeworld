from src.models.adresse import Adresse

class Utilisateur:

    def __init__(self, 
                 id: int,
                 nom: str,
                 prenom: str,
                 email: str,
                 password: str,
                 telephone: str
    ) -> None:
        """ Instanciation d'un Utilisateur

        Args:
            id (int): identifiant de l'utilisateur (pk)
            nom (str): Nom de l'utilisateur
            prenom (str): Prenom de l'utilisateur
            email (str): Email de l'utilisateur
            password (str): Mot de passe de l'utilisateur
            telephone (str): Numero de telephone de l'utilisateur
            adresse (Adresse): Adresse par defaut de l'utilisateur
        """
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.password = password
        self.telephone = telephone
        self.adresse: Adresse = None
