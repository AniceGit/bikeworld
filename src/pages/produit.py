import streamlit as st
import sqlite3
from pages.sidebar import afficher_sidebar
from models.produit import Produit
from controllers.produit_controller import get_details_produit


afficher_sidebar()
id= st.session_state["produit"].id
produit = get_details_produit(id)


st.title(produit.nom)


st.write(f"<span style='font-size: 20px;'>**Description**</span>: {produit.description}",unsafe_allow_html=True)
st.write(f"<span style='font-size: 20px;'>**Spécifications Techniques**</span>: {produit.spec_tech}",unsafe_allow_html=True)
st.write(f"<span style='font-size: 20px;'>**Couleur**</span>: {produit.couleur}",unsafe_allow_html=True)
st.write(f"<span style='font-size: 20px;'>**Prix**</span>: {produit.prix}",unsafe_allow_html=True)
st.write(f"<span style='font-size: 20px;'>**Stock**</span>: {produit.stock}",unsafe_allow_html=True)
if produit.image:
    st.image(produit.image, caption=produit.nom, use_container_width=True)
else:
    st.write("Aucune image disponible")

# Bouton pour ajouter au panier
if st.button("Ajouter au panier", key=produit):
    st.session_state.panier.append(produit)
    st.success(f"{produit['nom']} a été ajouté au panier !")

