import streamlit as st
import sqlite3
import json, os
from models.utilisateur import Utilisateur
from models.adresse import Adresse


# ----création d'un nouvel utilisateur via une inscription----#
def inscrire_utilisateur(
    nom: str, prenom: str, email: str, password: str, telephone: str
) -> bool:
    """
    Permet d'inscrire un nouvel utilisateur. Vérifie si l'email existe déjà dans la base de données,
    et crée un utilisateur si l'email est disponible.

    Paramètres:
    nom (str): Le nom de l'utilisateur.
    prenom (str): Le prénom de l'utilisateur.
    email (str): L'email de l'utilisateur (doit être unique).
    password (str): Le mot de passe de l'utilisateur.
    telephone (str): Le numéro de téléphone de l'utilisateur.

    Affiche un message de succès ou d'erreur via Streamlit.
    """
    utilisateur = get_utilisateur_by_email(email)
    if utilisateur:
        st.error("Cet email est déjà utilisé.")
        return False
    else:
        creer_utilisateur(nom, prenom, email, password, telephone)
        st.success("Inscription réussie. Vous pouvez maintenant vous connecter.")
        return True


def creer_utilisateur(
    nom: str, prenom: str, email: str, password: str, telephone: str
) -> None:
    """
    Crée un utilisateur dans la base de données SQLite en insérant ses informations dans la table 'utilisateur'.

    Paramètres:
    nom (str): Le nom de l'utilisateur.
    prenom (str): Le prénom de l'utilisateur.
    email (str): L'email de l'utilisateur.
    password (str): Le mot de passe de l'utilisateur.
    telephone (str): Le numéro de téléphone de l'utilisateur.
    """
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO utilisateur (nom, prenom, email, password, telephone)
            VALUES (:nom, :prenom, :email, :password, :telephone)
        """,
            {
                "nom": nom,
                "prenom": prenom,
                "email": email,
                "password": password,
                "telephone": telephone,
            },
        )


# ----connexion d'un utilisateur avec utilisation d'un get-email pour vérifier si cet utilisateur existe et s'il a ce password----#
def connecter_utilisateur(email: str, password: str) -> bool:
    """
    Permet de connecter un utilisateur en vérifiant ses identifiants (email et mot de passe).

    Paramètres:
    email (str): L'email de l'utilisateur.
    password (str): Le mot de passe de l'utilisateur.

    Affiche un message de succès ou d'erreur via Streamlit. Si les identifiants sont valides,
    l'utilisateur est enregistré dans la session.
    """
    utilisateur: Utilisateur = get_utilisateur_by_email(email)
    if utilisateur and utilisateur.password == password:
        st.session_state["utilisateur"] = utilisateur
        st.success(f"Bienvenue, {utilisateur.prenom} !")
        sauvegarder_json_utilisateur(utilisateur)
        return True
    else:
        st.error("Identifiants incorrects.")
        return False


def get_utilisateur_by_email(email: str) -> Utilisateur | None:
    """
    Récupère un utilisateur dans la base de données à partir de son email.

    Paramètres:
    email (str): L'email de l'utilisateur à rechercher.

    Retourne:
    tuple: Un tuple contenant les informations de l'utilisateur si l'email est trouvé,
           ou None si aucun utilisateur n'est trouvé avec cet email.
    """
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM utilisateur WHERE email = :email", {"email": email})
        result_utilisateur = cur.fetchone()
        if result_utilisateur:
            utilisateur: Utilisateur = Utilisateur(
                result_utilisateur[0],
                result_utilisateur[1],
                result_utilisateur[2],
                result_utilisateur[3],
                result_utilisateur[4],
                result_utilisateur[5],
            )

            cur.execute(
                "SELECT * FROM adresse WHERE id_utilisateur = :id_utilisateur AND defaut= :defaut",
                {"id_utilisateur": utilisateur.id, "defaut": 1},
            )
            result_adresse = cur.fetchone()
            if result_adresse:
                adresse: Adresse = Adresse(
                    result_adresse[0],
                    result_adresse[1],
                    result_adresse[2],
                    result_adresse[3],
                    result_adresse[4],
                    result_adresse[5],
                    result_adresse[6],
                    result_adresse[7],
                    result_adresse[8],
                )
                utilisateur.adresse = adresse
            return utilisateur
        return None


# -----Récupérer les adresses d'un utilisateur-----#
def get_adresses_utilisateur(id: int) -> list[Adresse]:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM adresse WHERE id_utilisateur = :id", {"id": id})
        result_adresses = cur.fetchall()
        if result_adresses is None:
            raise Exception(f"Aucune adresse")

        adresses = []
        for (
            id,
            numero,
            type_voie,
            nom_voie,
            code_postal,
            ville,
            pays,
            defaut,
            id_utilisateur,
        ) in result_adresses:
            adresses.append(
                Adresse(
                    id,
                    numero,
                    type_voie,
                    nom_voie,
                    code_postal,
                    ville,
                    pays,
                    defaut,
                    id_utilisateur,
                )
            )
        return adresses


def creer_adresse(
    numero: str,
    type_voie: str,
    nom_voie: str,
    code_postal: str,
    ville: str,
    pays: str,
    defaut: int,
    id_utilisateur: int,
) -> bool:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO adresse (numero, type_voie, nom_voie, code_postal, ville, pays, defaut, id_utilisateur)
            VALUES (:numero, :type_voie, :nom_voie, :code_postal, :ville, :pays, :defaut, :id_utilisateur)
        """,
            {
                "numero": numero,
                "type_voie": type_voie,
                "nom_voie": nom_voie,
                "code_postal": code_postal,
                "ville": ville,
                "pays": pays,
                "defaut": defaut,
                "id_utilisateur": id_utilisateur,
            },
        )
        st.success("Nouvelle adresse créée avec succès !")
        return True


# -----Modifier adresse-----#
def modifier_adresse_utilisateur(nouvelle_adresse: Adresse) -> None:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """UPDATE adresse SET numero = :numero, type_voie = :type_voie, nom_voie = :nom_voie, code_postal = :code_postal, ville = :ville, pays = :pays, defaut = :defaut WHERE id = :id_adresse
                    """,
            {
                "numero": nouvelle_adresse.numero,
                "type_voie": nouvelle_adresse.type_voie,
                "nom_voie": nouvelle_adresse.nom_voie,
                "code_postal": nouvelle_adresse.code_postal,
                "ville": nouvelle_adresse.ville,
                "pays": nouvelle_adresse.pays,
                "defaut": nouvelle_adresse.defaut,
                "id_adresse": nouvelle_adresse.id,
            },
        )


# -----modification de l'utilisateur-----#
def modifier_utilisateur(nouvel_utilisateur: Utilisateur) -> None:
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()
        cur.execute(
            """UPDATE utilisateur SET nom = :nom, prenom = :prenom, email = :email, telephone = :telephone WHERE id = :id_nouvel_utilisateur
                    """,
            {
                "nom": nouvel_utilisateur.nom,
                "prenom": nouvel_utilisateur.prenom,
                "email": nouvel_utilisateur.email,
                "telephone": nouvel_utilisateur.telephone,
                "id_nouvel_utilisateur": nouvel_utilisateur.id,
            },
        )
        sauvegarder_json_utilisateur(nouvel_utilisateur)


# -----déconnexion de l'utilisateur-----#
def deconnecter_utilisateur() -> str:
    if (
        "utilisateur" in st.session_state
        and st.session_state["utilisateur"] is not None
    ):
        prenom = st.session_state["utilisateur"].prenom
        st.session_state["utilisateur"] = None
        if os.path.exists("db/utilisateur_session.json"):
            supprimer_json_utilisateur()
    return prenom


# -----sauvegarde de l'utilisateur connecté dans un json-----#
def sauvegarder_json_utilisateur(utilisateur: Utilisateur) -> None:
    try:
        with open("db/utilisateur_session.json", "w") as f:
            json.dump(utilisateur.to_dict(), f)
    except Exception as e:
        st.error("Erreur de sauvegarde de session : " + str(e))


# -----supprimer le json utilisateur qui sert à session-----#
def supprimer_json_utilisateur() -> None:
    os.remove("db/utilisateur_session.json")



def get_utilisateur_by_id(id_utilisateur: int) -> Utilisateur | None:
    """
    Récupère un utilisateur dans la base de données à partir de son id.

    Paramètres:
    id_utilisateur (int): Identifiant de l'utilisateur à rechercher.

    Retourne:
    tuple: Un tuple contenant les informations de l'utilisateur si l'email est trouvé,
           ou None si aucun utilisateur n'est trouvé avec cet email.
    """
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cursor()

        cur.execute(
                """
                SELECT id, nom, prenom, email, password, telephone
                FROM utilisateur
                WHERE id = :id_utilisateur
            """,
                {"id_utilisateur": id_utilisateur}
            )

        result_utilisateur = cur.fetchone()

        id, nom, prenom, email, password, telephone = result_utilisateur
        utilisateur = Utilisateur(id, nom, prenom, email, password, telephone)

        return utilisateur
