import streamlit as st
from pages.sidebar import afficher_sidebar
from models.utilisateur import Utilisateur
from models.adresse import Adresse
from controllers.utilisateur_controller import modifier_utilisateur, sauvegarder_json_utilisateur, get_adresses_utilisateur, modifier_adresse_utilisateur

#Affichage sidebar et titre
afficher_sidebar()
st.title("Profil")

#Récupération des infos de l'utilisateur connecté
utilisateur:Utilisateur = st.session_state["utilisateur"]
adresse:Adresse = utilisateur.adresse

#Affichage du profil
st.write(f"Nom : {utilisateur.nom}")
st.write(f"Prénom : {utilisateur.prenom}")
st.write(f"Email : {utilisateur.email}")
st.write(f"Téléphone : {utilisateur.telephone}")
st.write(f"Adresse : {adresse.__str__()}")

if "nom_key" not in st.session_state or st.session_state.nom_key == "":
    st.session_state.nom_key = utilisateur.nom
if "prenom_key" not in st.session_state or st.session_state.prenom_key == "":
    st.session_state.prenom_key = utilisateur.prenom
if "email_key" not in st.session_state or st.session_state.email_key == "":
    st.session_state.email_key = utilisateur.email
if "telephone_key" not in st.session_state or st.session_state.telephone_key == "":
    st.session_state.telephone_key = utilisateur.telephone

#Input (on les vide au changement de page)
nom = st.text_input("Nom", key="nom_key")
prenom = st.text_input("Prénom", key="prenom_key")
email = st.text_input("Email", key="email_key")
telephone = st.text_input("Téléphone", key="telephone_key")

#On récupère toutes les adresses liées à cet utilisateur et on les met dans une liste
adresses:list[Adresse] = get_adresses_utilisateur(utilisateur.id)
option = st.selectbox(
    "Choisissez parmi vos adresses",
    (adresse.__str__() for adresse in adresses),
    index=None,
    placeholder="Choisir...",
)
button_disabled = option == None

#On affecte les valeurs insérées au nouvel utilisateur et on le modifie en db, session et json puis on refresh la page
if st.button("Modifier",disabled=button_disabled):
    nouvel_utilisateur = utilisateur
    nouvel_utilisateur.nom = nom if nom else utilisateur.nom
    nouvel_utilisateur.prenom = prenom if prenom else utilisateur.prenom
    nouvel_utilisateur.email = email if email else utilisateur.email
    nouvel_utilisateur.telephone = telephone if telephone else utilisateur.telephone

    #On récupère l'adresse selectionnée et on lui change sa valeur défaut pour en faire l'adresse par défaut puis on la modifie en db
    nouvelle_adresse:Adresse = next((adresse for adresse in adresses if adresse.__str__() == option),None)
    nouvelle_adresse.defaut = 1
    modifier_adresse_utilisateur(nouvelle_adresse)
    #On modifie la valeur défaut de l'adresse précédente (actuellement dans l'objet utilisateur) et on la modifie en db
    adresse.defaut = 0
    modifier_adresse_utilisateur(adresse)

    #On affecte l'adresse sélectionnée à l'objet nouvel_utilisateur qu'on sauvegardera en db, session et json
    nouvel_utilisateur.adresse = nouvelle_adresse

    modifier_utilisateur(nouvel_utilisateur)
    st.session_state["utilisateur"] = nouvel_utilisateur
    sauvegarder_json_utilisateur(nouvel_utilisateur)
    st.switch_page("pages/profil.py")
