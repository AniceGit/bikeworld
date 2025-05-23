import streamlit as st
from pages.sidebar import afficher_sidebar
from controllers.produit_controller import get_produits
from models.produit import Produit
import base64


afficher_sidebar()

st.title("Bienvenue sur la page des produits de BIKEWORLD!")


def set_bg_image(image_file: str) -> None:
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/{"png" if image_file.endswith(".png") else "jpg"};base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .custom-title {{
            color: #000000;  
        }}
        .custom-write {{
            color: #000000; 
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Chemin vers votre image de fond
image_file = "images/catalogue_background.jpg"  # Remplacez par le chemin de votre image

# Appliquer le fond d'écran
set_bg_image(image_file)

liste_produits: list[Produit] = get_produits()

# Définir le nombre de colonnes pour la grille
nb_colonnes = 4
colonnes = st.columns(nb_colonnes)

# Parcourir les produits et les afficher dans la grille
for i, produit in enumerate(liste_produits):
    column_index = i % nb_colonnes
    with colonnes[column_index]:
        if produit.image:
            st.image(produit.image, use_container_width=True)
            st.markdown(
                f"""
                <div style='background-color: #494341; padding: 4px; border-radius: 5px;'>
                    <p style='font-size: 24px; font-weight: bold; margin: 0;'>{produit.nom}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            prix_col, button_col = st.columns([1, 1])
            with prix_col:
                st.markdown(
                    f"<p style='font-size: 24px;'>Prix: {produit.prix:.2f} €</p>",
                    unsafe_allow_html=True,
                )
            with button_col:
                if st.button("Détail", key=produit.id):
                    st.session_state["produit"] = produit
                    st.switch_page("pages/produit.py")
        else:
            st.write("Aucune image disponible")
