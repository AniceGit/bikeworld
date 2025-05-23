import streamlit as st
from pages.sidebar import afficher_sidebar
from tools.session import init_session
import base64

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
        .custom-title {{
            color: #000000;  
        }}
        .custom-write {{
            color: #000000; 
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Chemin vers votre image de fond
image_file = "images/1223017.jpg"  # Remplacez par le chemin de votre image

# Appliquer le fond d'écran
set_bg_image(image_file)

# Configuration de la page
#st.set_page_config(page_title="BIKEWORLD", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def afficher_accueil():
    init_session()
    afficher_sidebar()

    st.markdown('<h1 class="custom-title">BIKEWORLD</h1>',unsafe_allow_html=True)
    st.write("The ways of Bithume")

    if st.button("Voir mes commandes"):
        st.switch_page("pages/commandes.py")


afficher_accueil()