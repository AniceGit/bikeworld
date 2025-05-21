import streamlit as st

st.title("Connexion")
st.write("Bienvenue sur la page de connexion de BIKEWORLD!")

# Bouton pour rediriger vers la page d'accueil
if st.button("Accueil"):
    st.query_params(page="Accueil")

# Bouton pour rediriger vers la page d'accueil
if st.button("Contact"):
    st.query_params(page="Catalogue")