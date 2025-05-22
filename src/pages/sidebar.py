import streamlit as st

def afficher_sidebar():

    # Initialisation de la session
    # if "utilisateur" not in st.session_state:
    #     st.session_state["utilisateur"] = None

    if st.session_state["utilisateur"] is None :
        st.sidebar.page_link("pages/connexion.py", label="Se connecter")
        st.sidebar.page_link("pages/inscription.py", label="S'inscrire")
    else :
        st.sidebar.text(f"👤 Connecté : {st.session_state["utilisateur"].prenom}")
        st.sidebar.page_link("pages/deconnexion.py", label="Se déconnecter")

    st.sidebar.text('toto')
    st.sidebar.page_link("pages/catalogue.py", label="Catalogue")
    st.sidebar.page_link("pages/panier.py", label="Panier")

