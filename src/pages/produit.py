import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import afficher_produit

afficher_sidebar()
st.title("Connexion")
st.write("Bienvenue sur la page de connexion de BIKEWORLD!")

if st.button("Voir mes commandes"):
    st.switch_page("pages/_commandes.py")

afficher_produit()