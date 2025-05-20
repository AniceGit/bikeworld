from adresse import Adresse

class Utilisateur:

    def __init__(self, 
                 id: int,
                 nom: str,
                 prenom: str,
                 email: str,
                 mdp: str,
                 tel: str
    ) -> None:
        """ Instanciation d'un Utilisateur

        Args:
            id (int): identifiant de l'utilisateur (pk)
            nom (str): Nom de l'utilisateur
            prenom (str): Prenom de l'utilisateur
            email (str): Email de l'utilisateur
            mdp (str): Mot de passe de l'utilisateur
            tel (str): Numero de telephone de l'utilisateur
        """
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.mdp = mdp
        self.tel = tel
        self.liste_adresse: list[Adresse] = []
