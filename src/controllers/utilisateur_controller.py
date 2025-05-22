import streamlit as st
import sqlite3

#----création d'un nouvel utilisateur via une inscription----#
def inscrire_utilisateur(nom, prenom, email, mdp, tel, adresse=None) -> None:
    """
    Permet d'inscrire un nouvel utilisateur. Vérifie si l'email existe déjà dans la base de données,
    et crée un utilisateur si l'email est disponible.

    Paramètres:
    nom (str): Le nom de l'utilisateur.
    prenom (str): Le prénom de l'utilisateur.
    email (str): L'email de l'utilisateur (doit être unique).
    mdp (str): Le mot de passe de l'utilisateur.
    tel (str): Le numéro de téléphone de l'utilisateur.
    adresse (str, optionnel): L'adresse de l'utilisateur (par défaut à None).

    Affiche un message de succès ou d'erreur via Streamlit.
    """
    utilisateur = get_utilisateur_by_email(email)
    if utilisateur:
        st.error("Cet email est déjà utilisé.")
    else:
        creer_utilisateur(nom, prenom, email, mdp, tel, adresse)
        st.success("Inscription réussie. Vous pouvez maintenant vous connecter.")

def creer_utilisateur(nom, prenom, email, mdp, tel, adresse) -> None:
    """
    Crée un utilisateur dans la base de données SQLite en insérant ses informations dans la table 'utilisateurs'.

    Paramètres:
    nom (str): Le nom de l'utilisateur.
    prenom (str): Le prénom de l'utilisateur.
    email (str): L'email de l'utilisateur.
    mdp (str): Le mot de passe de l'utilisateur.
    tel (str): Le numéro de téléphone de l'utilisateur.
    adresse (str): L'adresse de l'utilisateur (peut être None).
    """
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cur()
        cur.execute('''
            INSERT INTO utilisateurs (nom, prenom, email, mdp, tel, adresse)
            VALUES (:nom, :prenom, :email, :mdp, :tel, :adresse)
        ''', {'nom' : nom, 'prenom' : prenom, 'email' : email, 'mdp' : mdp, 'tel' : tel, 'adresse' : adresse})


#----connexion d'un utilisateur avec utilisation d'un get-email pour vérifier si cet utilisateur existe et s'il a ce mdp----#
def connecter_utilisateur(email, mdp) -> None:
    """
    Permet de connecter un utilisateur en vérifiant ses identifiants (email et mot de passe).

    Paramètres:
    email (str): L'email de l'utilisateur.
    mdp (str): Le mot de passe de l'utilisateur.

    Affiche un message de succès ou d'erreur via Streamlit. Si les identifiants sont valides, 
    l'utilisateur est enregistré dans la session.
    """
    utilisateur = get_utilisateur_by_email(email)
    if utilisateur and utilisateur[4] == mdp:
        st.session_state["utilisateur"] = utilisateur
        st.success(f"Bienvenue, {utilisateur[2]} !")
    else:
        st.error("Identifiants incorrects.")

def get_utilisateur_by_email(email) -> None:
    """
    Récupère un utilisateur dans la base de données à partir de son email.

    Paramètres:
    email (str): L'email de l'utilisateur à rechercher.

    Retourne:
    tuple: Un tuple contenant les informations de l'utilisateur si l'email est trouvé, 
           ou None si aucun utilisateur n'est trouvé avec cet email.
    """
    with sqlite3.connect("bikeworld.db") as conn:
        cur = conn.cur()
        cur.execute("SELECT * FROM utilisateurs WHERE email = ?", (email,))
        utilisateur = cur.fetchone()
        
        return utilisateur


#-----déconnexion de l'utilisateur-----#
def deconnecter_utilisateur() -> None:
    if "utilisateur" in st.session_state :
        prenom = st.session_state["utilisateur"][1]
        st.session_state["utilisateur"] = None
        st.success(f"Aurevoir, {prenom} !")