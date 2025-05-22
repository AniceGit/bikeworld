import streamlit as st
from models.utilisateur import Utilisateur
from models.adresse import Adresse


def init_session():
    if "utilisateur" not in st.session_state:
        st.session_state["utilisateur"] = None