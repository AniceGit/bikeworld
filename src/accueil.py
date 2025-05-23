import streamlit as st
from pages.sidebar import afficher_sidebar
from tools.session import init_session
from pages.bikeworld import afficher_produits_stars
import base64
#Affichage wide forcé
st.set_page_config(layout="wide")
#st.set_page_config(layout="wide")
def set_bg_image(image_file):
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
        </style>
        """,
        unsafe_allow_html=True
    )

# Chemin vers votre image de fond
image_file = "images/background_accueil_new.jpg"  # Remplacez par le chemin de votre image

# Appliquer le fond d'écran
set_bg_image(image_file)

def afficher_accueil():
    init_session()
    afficher_sidebar()
    afficher_produits_stars()

afficher_accueil()

