import streamlit as st
from pages.sidebar import afficher_sidebar
from tools.session import init_session

# Configuration de la page
st.set_page_config(page_title="BIKEWORLD", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# Fonction pour injecter le CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Appeler la fonction pour injecter le CSS
local_css("style.css")

def afficher_accueil():

    init_session()
    afficher_sidebar()

    st.title("Page d'Accueil")
    st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")

    if st.button("Voir mes commandes"):
        st.switch_page("pages/commandes.py")

afficher_accueil()