import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.commande_controller import supprimer_commande


afficher_sidebar()
st.title("Commandes")
st.write("Bienvenue sur la page de commandes de BIKEWORLD!")

supprimer_commande(2)

