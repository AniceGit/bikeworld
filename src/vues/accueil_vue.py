import streamlit as st

st.write("Bienvenue sur la page d'accueil de BIKEWORLD!")

# Bouton pour rediriger vers la page de Catalogue(produit)
if st.button("Produits"):
    st.query_params(page="Produits")