import streamlit as st
from pages.sidebar import afficher_sidebar
from models.utilisateur import Utilisateur
from models.adresse import Adresse

afficher_sidebar()
st.title("Profil")

utilisateur:Utilisateur = st.session_state["utilisateur"]
adresse:Adresse = utilisateur.adresse

st.write(f"Nom : {utilisateur.nom}")
st.write(f"Prénom : {utilisateur.prenom}")
st.write(f"Email : {utilisateur.email}")
st.write(f"Téléphone : {utilisateur.telephone}")
st.write(f"Adresse : {adresse.numero} {adresse.type_voie} {adresse.nom_voie} - {adresse.code_postal} {adresse.ville} - {adresse.pays}")


