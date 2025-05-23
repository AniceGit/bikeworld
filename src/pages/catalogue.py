import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import get_produits
from models.produit import Produit

afficher_sidebar()

st.title("Bienvenue sur la page des produits de BIKEWORLD!")

liste_produits:list[Produit] = get_produits()

# Définir le nombre de colonnes pour la grille
nb_colonnes = 4
colonnes = st.columns(nb_colonnes)

# Parcourir les produits et les afficher dans la grille
for i, produit in enumerate(liste_produits):
    column_index = i % nb_colonnes
    with colonnes[column_index]:   
        
        if produit.image:
            st.image(produit.image, caption=produit.nom, use_container_width=True)
            st.write(f"Prix: {produit.prix}")
            if st.button("DETAIL", key=produit.id):
                st.session_state["produit"]=produit
                st.switch_page("pages/produit.py")
        else:
            st.write("Aucune image disponible")
        