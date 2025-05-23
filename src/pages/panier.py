import streamlit as st
import pandas as pd
from pages.sidebar import afficher_sidebar
from src.tools.session import init_session


init_session()
afficher_sidebar()
st.title("Mon Panier")


panier = st.session_state.panier

if panier:
    st.write(f"Date: {panier["date_panier"]}")

    df_total = pd.DataFrame([{
        "Total du panier (€)": f"{panier["total_panier"]:.2f}",
    }])
    
    df = pd.DataFrame([{
                "Produit": produit_quantite["produit"],
                "Quantité": produit_quantite["quantite"],
                "Prix unitaire (€)": f"{produit_quantite["prix"]:.2f}",
                "Total (€)": f"{produit_quantite["total"]:.2f}"
            } for produit_quantite in panier["liste_produits_quantite"]])

    st.dataframe(df, column_config={
#        "Produit": st.column_config.LinkColumn("Produit")
        "Prix unitaire (€)": st.column_config.NumberColumn(format="euro"),
        "Total (€)": st.column_config.NumberColumn(format="euro")
    }, hide_index=True)

    st.dataframe(df_total, column_config={
        "Total du panier (€)": st.column_config.NumberColumn(format="euro"),
    }, hide_index=True)

if st.button("Passer la commande"):
    if not st.session_state["utilisateur"]:
        st.switch_page("pages/connexion.py")
    else:
        pass

