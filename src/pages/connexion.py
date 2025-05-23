import streamlit as st
import time
from src.controllers.utilisateur_controller import connecter_utilisateur
from pages.sidebar import afficher_sidebar
import base64

afficher_sidebar()

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
        .stTextInput>div>div>label {{
            color: #000000;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Chemin vers votre image de fond
image_file = "images/333354.jpg"  # Remplacez par le chemin de votre image

# Appliquer le fond d'écran
set_bg_image(image_file)

st.markdown('<h1 class="custom-title">Page de Connexion</h1>', unsafe_allow_html=True)
st.markdown('<p class="custom-write">Bienvenue sur la page de connexion de BIKEWORLD!</p>', unsafe_allow_html=True)

def connexion_vue():
    st.markdown('<p class="custom-write">Connexion</p>', unsafe_allow_html=True)

    email = st.text_input("Email")
    mdp = st.text_input("Mot de passe")

    if st.button("Se connecter"):
        if email and mdp:
            if connecter_utilisateur(email, mdp):
                time.sleep(2)
                st.switch_page("accueil.py")
        else :
            st.markdown('<p class="custom-write">Veuillez saisir vos informations personnelles</p>', unsafe_allow_html=True)

connexion_vue()
