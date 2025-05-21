import streamlit as st

from src.tools.session import init_session
from menu_vue import afficher_menu
from src.pages.connexion import connexion_vue
from src.pages.inscription import inscrire_vue
from src.pages.accueil import afficher_accueil


init_session()

page = afficher_menu()

if page == "Connexion":
    connexion_vue()
elif page == "Inscription":
    inscrire_vue()
else:
    afficher_accueil()
    st.write("Bienvenue sur la page d’accueil !")
