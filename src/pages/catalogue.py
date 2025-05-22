import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import get_produits
from models.produit import Produit
from controllers.produit_controller import get_details_produit

afficher_sidebar()


st.write("Bienvenue sur la page des produits de BIKEWORLD!")

liste_produits:list[Produit] = get_produits()


# Définir le nombre de colonnes pour la grille
nb_colonnes = 2
colonnes = st.columns(nb_colonnes)

# Parcourir les produits et les afficher dans la grille
for i, produit in enumerate(liste_produits):
    column_index = i % nb_colonnes
    with colonnes[column_index]:   
        st.write(f"Nom: {produit.nom}, Prix: {produit.prix}")
        if produit.image:
            st.image(produit.image, caption=produit.nom, use_container_width=True)
            # Ajouter un bouton transparent superposé à l'image
            # if st.button(f"Voir Détails", key=f"btn_{produit.id}"):
            #     get_details_produit(produit.id)
            if st.button("DETAIL", key=produit.id):
                st.session_state["produit"]=produit
                st.switch_page("pages/produit.py")
        else:
            st.write("Aucune image disponible")