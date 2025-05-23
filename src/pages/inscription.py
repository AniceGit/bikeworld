import streamlit as st
import time
from src.controllers.utilisateur_controller import inscrire_utilisateur
from pages.sidebar import afficher_sidebar

afficher_sidebar()

st.title("Page de d'inscription")
st.write("Bienvenue sur la page d'insciption de BIKEWORLD!")


def inscrire_vue() -> None:
    st.header("Inscription")

    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    tel = st.text_input("Téléphone")
    email = st.text_input("Email")
    mdp = st.text_input("Mot de passe")

    if st.button("S'inscrire"):
        if nom and prenom and tel and email and mdp:
            if inscrire_utilisateur(nom, prenom, email, mdp, tel):
                time.sleep(2)
                st.switch_page("pages/connexion.py")
        else:
            st.write("Veuillez saisir vos informations personnelles")


inscrire_vue()
