import streamlit as st

def init_session():
    if "utilisateur" not in st.session_state:
        st.session_state["utilisateur"] = None
    st.session_state["panier"] = None
    st.session_state["produit"] = None
