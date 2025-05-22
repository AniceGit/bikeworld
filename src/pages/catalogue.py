import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import afficher_produits


afficher_sidebar()

st.title("Page des Produits")
st.write("Bienvenue sur la page des produits de BIKEWORLD!")

liste_produits = afficher_produits()