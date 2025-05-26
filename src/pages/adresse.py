import streamlit as st
import time
from pages.sidebar import afficher_sidebar
from models.utilisateur import Utilisateur
from controllers.utilisateur_controller import creer_adresse
from src.tools.session import init_session

init_session()

# Affichage sidebar et titre
afficher_sidebar()
st.title("Ajout d'une nouvelle adresse")
if st.button("Profil"):
    st.switch_page("pages/profil.py")

# Récupération des infos de l'utilisateur connecté
utilisateur: Utilisateur = st.session_state["utilisateur"]

# Input (on les vide au changement de page)
numero = st.text_input("Numéro")
type_voie = st.text_input("Type de voie")
nom_voie = st.text_input("Nom de voie")
code_postal = st.text_input("Code Postal")
ville = st.text_input("Ville")
pays = st.text_input("Pays")

# On affecte les valeurs insérées au nouvel utilisateur et on le modifie en db, session et json puis on refresh la page
if st.button("Ajouter"):
    if numero and type_voie and nom_voie and code_postal and ville and pays:
        if creer_adresse(
            numero, type_voie, nom_voie, code_postal, ville, pays, 0, utilisateur.id
        ):
            with st.spinner(text="Veuillez patienter", show_time=False):
                time.sleep(2)
            st.switch_page("pages/profil.py")
    else:
        st.write("Veuillez saisir votre adresse complète")
