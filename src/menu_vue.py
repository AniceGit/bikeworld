import streamlit as st


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

# Fonction pour afficher le menu horizontalement
def afficher_menu_horizontal(menu):
    cols = st.columns(len(menu))
    for idx, (item, sous_menu) in enumerate(menu.items()):
        with cols[idx]:
            if sous_menu:  # Si l'item a un sous-menu
                if st.button(item):
                    afficher_sous_menu_vertical(sous_menu)
            else:
                if st.button(item):
                    if item == "Accueil":
                            st.query_params(page="Accueil")
                    elif item == "Catalogue":
                            st.query_params(page="Catalogue")
                    elif item == "Produits":
                            st.query_params(page="Produits")
                    elif item == "Produits":
                            st.query_params(page="Produits")
                    elif item == "Produits":
                            st.query_params(page="Produits")
                    elif item == "Produits":
                            st.query_params(page="Produits")

# Fonction pour afficher les sous-menus verticalement
def afficher_sous_menu_vertical(sous_menu):
    for item, sous_sous_menu in sous_menu.items():
        if sous_sous_menu:  # Si l'item a un sous-sous-menu
            if st.button(item):
                afficher_sous_menu_vertical(sous_sous_menu)
        else:
            if st.button(item):
                if item == "Accueil":
                        st.query_params(page="Accueil")
                elif item == "Produits":
                        st.query_params(page="Produits")

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

# Afficher le menu en haut
#st.write("### Menu")
afficher_menu_horizontal(menu_bikeworld)

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
