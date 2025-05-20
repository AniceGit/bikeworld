import streamlit as st


# Définir le CSS personnalisé pour le fond d'écran
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

# Importer la bibliothèque base64 pour encoder l'image
import base64

# Chemin vers votre image de fond
image_file = "1223017.jpg"  # Remplacez par le chemin de votre image

# Appliquer le fond d'écran
set_bg_image(image_file)


# Ajouter un titre
st.title("BIKEWORLD - L'endroit où la roue tourne !")

# Ajouter du texte
st.write("Bonjour, bienvenue dans mon application Streamlit!")

# Définir les pages
pages = [
    st.Page("1_Homepage.py", title="Home", default=True),
    st.Page("2_Catalogue.py", title="Catalogue", url_path="settings")
]
pg = st.navigation(pages)
# Ajouter un widget de texte
name = st.text_input("Quel est votre nom?")
if name:
    st.write(f"Bonjour, {name}!")

# Ajouter un bouton
if st.button("Cliquez ici"):
    st.write("Vous avez cliqué sur le bouton!")

# Ajouter un sélecteur
option = st.selectbox("Choisissez une option", ["Option 1", "Option 2", "Option 3"])
st.write(f"Vous avez choisi: {option}")

#st.switch_page("2_Catalogue.py")


# Utiliser st.navigation

pg.run()