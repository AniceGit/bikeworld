import streamlit as st
import time
from pages.sidebar import afficher_sidebar
from src.controllers.utilisateur_controller import deconnecter_utilisateur

afficher_sidebar()

prenom = deconnecter_utilisateur()
if prenom is not None:
    with st.spinner(text="Veuillez patienter", show_time=False):
        st.success(f"Au revoir {prenom} !")
        time.sleep(2)
    st.switch_page("accueil.py")
else : 
    st.info("Vous n'étiez pas connecté")
