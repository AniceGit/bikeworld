from src.models.adresse import Adresse
from src.models.adresse import adresse_from_dict
import sqlite3

class Utilisateur:

    def __init__(
        self, id: int, nom: str, prenom: str, email: str, password: str, telephone: str
    ) -> None:
        """Instanciation d'un Utilisateur

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
        self.roles: list = get_roles(self.id)


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "email": self.email,
            "password": self.password,
            "telephone": self.telephone,
            "adresse": self.adresse.to_dict() if self.adresse else None,
            "roles": self.roles if self.roles else []
        }


    def is_admin(self) -> bool:
        return True if "admin" in self.roles else False


    def is_superclient(self) -> bool:
        return True if "superclient" in self.roles else False


def utilisateur_from_dict(data) -> Utilisateur:
    utilisateur = Utilisateur(
        data["id"],
        data["nom"],
        data["prenom"],
        data["email"],
        data["password"],
        data["telephone"],
    )
    if data.get("adresse"):
        utilisateur.adresse = adresse_from_dict(data["adresse"])

    utilisateur.roles = get_roles(data["id"])
    return utilisateur


def get_roles(id_utilisateur) -> list:

    roles = []
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        # Récupération des roles de l'utilisateur
        cur.execute("""
            SELECT id_role
            FROM roles_utilisateur
            WHERE id_utilisateur = :id_utilisateur
        """,
            {"id_utilisateur": id_utilisateur},
        )
        roles_id = cur.fetchall()

        for id_roles in roles_id:
            # Récupération des noms des roles
            cur.execute(
                """
                SELECT nom
                FROM roles
                WHERE id = :id
            """,
                {"id": id_roles[0]},
            )
            result_roles = cur.fetchall()

            for nom in result_roles:
                roles.append(nom[0])

    return roles


