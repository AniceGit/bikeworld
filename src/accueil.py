import streamlit as st
from pages.sidebar import afficher_sidebar

def afficher_accueil():

    afficher_sidebar()

    st.title("Page d'Accueil")
    st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")


    if st.button("Voir mes commandes"):
        st.switch_page("pages/commandes.py")


afficher_accueil()
