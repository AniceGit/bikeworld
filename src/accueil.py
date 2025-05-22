import streamlit as st
from pages.sidebar import afficher_sidebar

# Configuration de la page
st.set_page_config(page_title="BIKEWORLD", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def afficher_accueil():

    afficher_sidebar()

    st.title("Page d'Accueil")
    st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")


    if st.button("Voir mes commandes"):
        st.switch_page("pages/commandes.py")


afficher_accueil()
