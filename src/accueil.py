import streamlit as st
from pages.sidebar import afficher_sidebar
from tools.session import init_session

# Configuration de la page
st.set_page_config(page_title="BIKEWORLD", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def afficher_accueil():
    init_session()
    afficher_sidebar()

    st.title("Page d'Accueil")
    st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")

afficher_accueil()