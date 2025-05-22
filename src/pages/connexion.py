import streamlit as st
from src.controllers.utilisateur_controller import connecter_utilisateur
from pages.sidebar import afficher_sidebar


afficher_sidebar()

st.title("Page de Connexion")
st.write("Bienvenue sur la page de connexion de BIKEWORLD!")



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
