import streamlit as st


menu_bikeworld = {
    "Accueil": {},
    "Produits": {
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
                    st.write(f"Vous avez sélectionné: {item}")

# Fonction pour afficher les sous-menus verticalement
def afficher_sous_menu_vertical(sous_menu):
    for item, sous_sous_menu in sous_menu.items():
        if sous_sous_menu:  # Si l'item a un sous-sous-menu
            if st.button(item):
                afficher_sous_menu_vertical(sous_sous_menu)
        else:
            if st.button(item):
                st.write(f"Vous avez sélectionné: {item}")

# Ajouter du CSS pour ajuster la largeur de la colonne principale
st.markdown(
    """
    <style>
    .main > div {
        max-width: 100%;
        padding-left: 0;
        padding-right: 0;
    }
    .stTitle {
        width :100%;
        text-align : center;
        margin-bottom : 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Ajouter un titre
st.markdown("<h1 class='stTitle'>BIKEWORLD - L'endroit où la roue tourne !</h1>", unsafe_allow_html=True)

# Afficher le menu en haut
st.write("### Menu")
afficher_menu_horizontal(menu_bikeworld)


