import streamlit as st


def afficher_sidebar() -> None:

    if st.sidebar.button("🚴🏻 **BikeWorld** 🚴🏻", use_container_width=True):
        st.switch_page("accueil.py")

    if st.session_state["utilisateur"] is None:
        st.sidebar.page_link("pages/connexion.py", label="⏻ Se connecter")
        st.sidebar.page_link("pages/inscription.py", label="S'inscrire")
    else:
        st.sidebar.text(f"Connecté : {st.session_state['utilisateur'].prenom}")
        st.sidebar.page_link("pages/profil.py", label="👤 Profil")
        st.sidebar.page_link("pages/commandes.py", label="📦 Mes commandes")
        st.sidebar.page_link("pages/deconnexion.py", label="⏻ Se déconnecter")
        if st.session_state["utilisateur"].is_admin():
            st.sidebar.text("ADMIN")
            st.sidebar.page_link("pages/admin_commandes.py", label="Admin Commandes")

    st.sidebar.text("SHOP")
    st.sidebar.page_link("pages/catalogue.py", label="Catalogue")
    st.sidebar.page_link("pages/panier.py", label="Panier")

