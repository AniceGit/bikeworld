import streamlit as st


def afficher_sidebar():
    
    st.sidebar.page_link("pages/connexion.py", label="Se connecter")
    st.sidebar.page_link("pages/inscription.py", label="Inscription")

    st.sidebar.text('SHOP')
    st.sidebar.page_link("pages/catalogue.py", label="Catalogue")
    st.sidebar.page_link("pages/panier.py", label="Panier")

    # st.page_link("pages/panier.py", label="Panier")

    # with st.popover("Categories"):
    #     st.page_link("pages/commandes.py", label="Commandes")
    #     st.page_link("pages/panier.py", label="Panier")
