import streamlit as st

st.title("Page de Connexion")
st.write("Bienvenue sur la page de connexion de BIKEWORLD!")

# Utiliser st.columns pour afficher les boutons horizontalement
cols = st.columns(3)  # Ajustez le nombre de colonnes selon le nombre de pages
pages = [
    ("Accueil", "./accueil.py"),
    ("Produits", "./catalogue.py"),
    ("Connexion", "./connexion.py"),
    ("inscription", "./inscription.py"),
    ("panier", "./panier.py"),
    ("produit", "./produit.py"),
    ("profil", "./profil.py")
]

for idx, (title, page) in enumerate(pages):
    with cols[idx]:
        if st.button(title):
            st.switch_page(page)
from src.controllers.utilisateur_controller import connecter_utilisateur

def connexion_vue():
    st.header("Connexion")

    email = st.text_input("Email")
    mdp = st.text_input("Mot de passe")

    if st.button("Se connecter"):
        if email and mdp:
            connecter_utilisateur(email, mdp)
        else :
            st.write("Veuillez saisir vos informations personnelles")

#connexion_vue()
