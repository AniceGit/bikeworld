import streamlit as st

def init_session():
    if "utilisateur" not in st.session_state:
        #st.session_state["utilisateur"] = None
        st.session_state["utilisateur"] = ("Dujardin", "Jean", "test@email.com", "mymdp", "0684452195", "adresse")
