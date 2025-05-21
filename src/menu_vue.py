import streamlit as st

# Configuration de la page
st.set_page_config(page_title="BIKEWORLD", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

# Ajouter du CSS pour ajuster la largeur de la colonne principale
st.markdown(
    """
    <style>
        .main > div {
            max-width: 100%;
            padding-left: 10rem;
            padding-right: 10rem;
        }
        .stTitle {
            width: 100%;
            text-align: center;
            margin-bottom: 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Ajouter un titre
st.markdown("<h1 class='stTitle'>BIKEWORLD - L'endroit où la roue tourne !</h1>", unsafe_allow_html=True)

# Utiliser st.columns pour afficher les boutons horizontalement
cols = st.columns(3)  # Ajustez le nombre de colonnes selon le nombre de pages
pages = [
    ("Accueil", "pages/accueil_vue.py"),
    ("Produits", "pages/catalogue_vue.py"),
    ("Connexion", "pages/connexion_vue.py")
]

for idx, (title, page) in enumerate(pages):
    with cols[idx]:
        if st.button(title):
            st.switch_page(page)
