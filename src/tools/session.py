import streamlit as st
import json, os, datetime
from models.utilisateur import utilisateur_from_dict


def init_session() -> None:
    if "utilisateur" not in st.session_state:
        if os.path.exists("db/utilisateur_session.json"):
            try:
                with open("db/utilisateur_session.json", "r") as f:
                    data = json.load(f)
                    st.session_state["utilisateur"] = utilisateur_from_dict(data)
            except json.JSONDecodeError:
                # Fichier corrompu ou vide → on le supprime
                os.remove("db/utilisateur_session.json")
                st.session_state["utilisateur"] = None
        else:
            st.session_state["utilisateur"] = None

    if "produit" not in st.session_state:
        st.session_state["produit"] = None

    if "panier" not in st.session_state:
        st.session_state.panier = {
            "date_panier": str(datetime.date.today()),
            "total_panier": 0.0,
            "frais_livraison": 20.0,
            "liste_produits_quantite": []
        }
