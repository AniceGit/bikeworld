import streamlit as st
import datetime

def init_session():
    if "utilisateur" not in st.session_state:
        st.session_state["utilisateur"] = None

    if "produit" not in st.session_state:
        st.session_state["produit"] = None

    if "panier" not in st.session_state:
        st.session_state.panier = {
            "date_panier": str(datetime.date.today()),
            "total_panier": 0.0,
            "liste_produits_quantite": []
        }
