import streamlit as st

st.title("Page de d'inscription")
st.write("Bienvenue sur la page d'insciption de BIKEWORLD!")

from src.controllers.utilisateur_controller import inscrire_utilisateur

def inscrire_vue():
    st.header("Inscription")

    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    tel = st.text_input("Téléphone")
    #adresse = st.text_input("Adresse")
    email = st.text_input("Email")
    mdp = st.text_input("Mot de passe")

    if st.button("S'inscrire"):
        if nom and prenom and tel and email and mdp :
            inscrire_utilisateur(nom, prenom, email, mdp, tel)
        else :
            st.write("Veuillez saisir vos informations personnelles")

#inscrire_vue()
