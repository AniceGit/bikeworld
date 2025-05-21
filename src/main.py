import streamlit as st

from src.tools.session import init_session
from src.vues.menu_vue import afficher_menu
from src.vues.connexion_vue import connexion_vue
from src.vues.inscription_vue import inscrire_vue
from src.vues.accueil_vue import afficher_accueil


init_session()

page = afficher_menu()

if page == "Connexion":
    connexion_vue()
elif page == "Inscription":
    inscrire_vue()
else:
    afficher_accueil()
    st.write("Bienvenue sur la page d’accueil !")
