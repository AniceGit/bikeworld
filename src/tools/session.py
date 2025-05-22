import streamlit as st
from src.models.utilisateur import Utilisateur
from src.models.adresse import Adresse


def init_session():
    if "utilisateur" not in st.session_state:
        st.session_state["panier"] = None
#        st.session_state["utilisateur"] = None
        adresse = Adresse(
            1, "10", "rue", "de la Convention", "75015", "Paris", "France", 1, 1
        )
        st.session_state["utilisateur"] = Utilisateur(
            1,
            "Guiren",
            "Anice",
            "anice@example.com",
            "testAnice",
            "07.06.05.04.03",
            adresse,
        )

        st.session_state["produit"] = None
