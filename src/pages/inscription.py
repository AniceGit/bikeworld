import streamlit as st

st.title("Page de d'inscription")
st.write("Bienvenue sur la page d'insciption de BIKEWORLD!")

# Utiliser st.columns pour afficher les boutons horizontalement
cols = st.columns(3)  # Ajustez le nombre de colonnes selon le nombre de pages
pages = [
    ("Accueil", "./accueil.py"),
    ("Produits", "./catalogue.py"),
    ("Connexion", "./connexion.py"),
    ("inscription", "./inscription.py"),
    ("panier", "./panier.py"),
    ("produit", "./produit.py"),
    ("profil", "./profil.py")
]

for idx, (title, page) in enumerate(pages):
    with cols[idx]:
        if st.button(title):
            st.switch_page(page)