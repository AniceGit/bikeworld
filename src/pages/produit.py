import streamlit as st
import sqlite3
from pages.sidebar import afficher_sidebar
from models.produit import Produit
from controllers.produit_controller import get_details_produit


afficher_sidebar()
id= st.session_state["produit"].id
produit = get_details_produit(id)


st.title(produit.nom)


st.write(f"Description: {produit.description}")
st.write(f"Spécifications Techniques: {produit.spec_tech}")
st.write(f"Couleur: {produit.couleur}")
st.write(f"Prix: {produit.prix}")
st.write(f"Stock: {produit.stock}")
if produit.image:
    st.image(produit.image, caption=produit.nom, use_container_width=True)
else:
    st.write("Aucune image disponible")

