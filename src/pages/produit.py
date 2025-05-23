import streamlit as st
import sqlite3
from pages.sidebar import afficher_sidebar
from models.produit import Produit
from controllers.produit_controller import get_details_produit
from src.tools.session import init_session


init_session()
afficher_sidebar()
id = st.session_state["produit"].id
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
if st.button("Ajouter au panier", key=produit.id):
    panier = st.session_state.panier

    if panier:
        for produit_quantite in panier["liste_produits_quantite"]:
            p_id = produit_quantite["produit_id"]

            if p_id == produit.id:
                produit_quantite["quantite"] += 1
                panier["total_panier"] += produit.prix
                panier["total_panier"] = round(panier["total_panier"],2)
                produit_quantite["total"] = produit.prix * produit_quantite["quantite"]
                produit_quantite["total"] = round(produit_quantite["total"],2)
                st.session_state.panier = panier
                print(st.session_state.panier)
                break
        
        else:
            panier["total_panier"] += produit.prix
            panier["total_panier"] = round(panier["total_panier"],2)
            panier["liste_produits_quantite"].append({"produit_id": produit.id, "produit": produit.nom, "quantite": 1, "prix": produit.prix, "total": produit.prix})
            st.session_state.panier = panier
            print(st.session_state.panier)


    # st.success(f"{produit['nom']} a été ajouté au panier !")
