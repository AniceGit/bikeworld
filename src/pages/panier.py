import streamlit as st
from pages.sidebar import afficher_sidebar
from src.tools.session import init_session
from src.models.panier import Panier
from src.models.produit import Produit


init_session()
afficher_sidebar()
st.title("Mon Panier")


# produit1 = Produit()

# liste_p_q = [()]

# panier = Panier("2025-05-20", 2997.00, )
# st.session_state["panier"] = panier

if not st.session_state["panier"]:
    st.subheader(f"🧾 Votre panier est vide")
else:
    st.subheader(f"🧾 Détails du panier")
    st.write(f"Date : {st.session_state["panier"].date_panier}")

    for produit_panier, quantite in st.session_state["panier"].liste_produits_quantite:
        print(f"Produit: {produit_panier}, Quantité: {quantite}")

