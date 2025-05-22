import streamlit as st
from pages.sidebar import afficher_sidebar
from tools.session import init_session

def afficher_accueil():

    init_session()
    afficher_sidebar()

    st.title("Page d'Accueil")
    st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")

    if st.button("Voir mes commandes"):
        st.switch_page("pages/commandes.py")

afficher_accueil()