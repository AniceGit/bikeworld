import streamlit as st

# Bouton pour rediriger vers la page d'accueil
if st.button("Accueil"):
    st.query_params(page="Accueil")
