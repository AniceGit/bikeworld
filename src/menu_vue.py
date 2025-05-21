import streamlit as st

from src.controllers.utilisateur_controller import deconnecter_utilisateur

menu_bikeworld = {
    "Accueil": {},
    "Catalogue": {
        "Vélo": {
            "VTT":{},
            "BMX":{},
            "Route":{}           
        },
        "Equipement": {
            "Casques":{},
            "Chaussures":{},
            "Accessoires":{}
        },
        "Marques": {
            "Specialized":{},
            "Giant":{},
            "Scott":{},
            "Decathlon":{}
        }
    },
    "Contact": {},
    "Mon Compte":{}
}

st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

#Ajouter du CSS pour ajuster la largeur de la colonne principale
st.markdown(
    """
        <style>
            .main > div {
            max-width: 100%;
            padding-left: 10rem;
            padding-right: 10rem;
        }
        .stTitle {
            width :100%;
            text-align : center;
            margin-bottom : 0;
        }

        </style>
    """,
    unsafe_allow_html=True
)

# Ajouter un titre
st.markdown("<h1 class='stTitle'>BIKEWORLD - L'endroit où la roue tourne !</h1>", unsafe_allow_html=True)

# Gestion de la connexion dans la sidebar
if st.session_state["utilisateur"] is not None:
    utilisateur = st.session_state["utilisateur"]
    st.sidebar.markdown(f"Connecté : {utilisateur[0]} {utilisateur[1]}")
    if st.sidebar.button("Déconnexion"):
        deconnecter_utilisateur()
else:
    col1, col2 = st.sidebar.columns(2)
    with col1:
        if st.button("Connexion"):
            st.switch_page("pages/connexion.py")
    with col2:
        if st.button("Inscription"):
            st.switch_page("pages/inscription.py")

cols = st.columns(3)  # Ajustez le nombre de colonnes selon le nombre de pages
pages = [
    ("Accueil", "pages/accueil.py"),
    ("Produits", "pages/catalogue.py"),
    ("Connexion", "pages/connexion.py"),
    ("inscription", "pages/inscription.py"),
    ("panier", "pages/panier.py"),
    ("produit", "pages/produit.py"),
    ("profil", "pages/profil.py")
]

for idx, (title, page) in enumerate(pages):
    with cols[idx]:
        if st.button(title):
            st.switch_page(page)

pg = st.navigation(pages)
pg.run()