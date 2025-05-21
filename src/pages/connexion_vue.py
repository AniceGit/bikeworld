import streamlit as st

st.title("Page de Connexion")
st.write("Bienvenue sur la page de connexion de BIKEWORLD!")

# Utiliser st.columns pour afficher les boutons horizontalement
cols = st.columns(3)  # Ajustez le nombre de colonnes selon le nombre de pages
pages = [
    ("Accueil", "./accueil_vue.py"),
    ("Produits", "./catalogue_vue.py"),
    ("Connexion", "./connexion_vue.py")
]

for idx, (title, page) in enumerate(pages):
    with cols[idx]:
        if st.button(title):
            st.switch_page(page)
