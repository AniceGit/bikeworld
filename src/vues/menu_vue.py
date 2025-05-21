import streamlit as st
from src.controllers.utilisateur_controller import deconnecter_utilisateur

def afficher_menu():
    st.sidebar.title("Menu")

    if st.session_state["utilisateur"] is not None:
        utilisateur = st.session_state["utilisateur"]
        st.sidebar.markdown(f"Connecté : **{utilisateur[0]} {utilisateur[1]}**")
        if st.sidebar.button("Déconnexion"):
            deconnecter_utilisateur()
        #return "Accueil"
        st.session_state["page"] = "Acueil"
    else:
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("Connexion"):
                st.session_state["page"] = "Connexion"
        with col2:
            if st.button("Inscription"):
                st.session_state["page"] = "Inscription"

        return st.session_state.get("page", "Connexion")
