import streamlit as st

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

# Utiliser st.navigation

pg.run()